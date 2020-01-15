import asyncio
import json
import logging
from timeit import default_timer

import async_timeout
from aiohttp import BasicAuth, ClientSession
from aiohttp.hdrs import USER_AGENT, ACCEPT

from ..const import CLIENT_USER_AGENT, APPLICATION_JSON, BASE_URL

_LOGGER = logging.getLogger(__name__)

KEY_RESPONSE = 'resp'
KEY_ATTR = 'url'
KEY_ELAPSED = 'elapsed'

ATTR_RECIPES = 'recipes'
ATTR_RECIPE_ITEMS = 'recipe_items'
RECIPE_ENDPOINT = 'recipe/%s'

ENDPOINTS = [
    'bookmarks',
    'categories',
    'groceries',
    'meals',
    'menus',
    'menuitems',
    'pantry',
    ATTR_RECIPES,
    'status'
]


async def _fetch(url, session, attr_override=None):
    """ Fetch a single URL """

    with async_timeout.timeout(10):
        async with session.get("%s%s" % (BASE_URL, url)) as response:
            before_request = default_timer()
            resp = await response.read()
            elapsed = default_timer() - before_request

            return {
                KEY_RESPONSE: json.loads(resp).get("result"),
                KEY_ATTR: url if not attr_override else attr_override,
                KEY_ELAPSED: elapsed
            }


class PaprikaClient:
    """Client to connect to Paprika backend servers."""

    last_fetch_timestamp = None

    def __init__(self, username, password):
        """Initialize the client."""
        self._auth = BasicAuth(
            login=username,
            password=password
        )
        self._headers = {
            USER_AGENT: CLIENT_USER_AGENT,
            ACCEPT: APPLICATION_JSON
        }

    def _process_responses(self, results):
        """Process the responses from fetch_all."""
        for result in results:
            url = result[KEY_ATTR]
            response = result[KEY_RESPONSE]

            self.__setattr__(url, response)

    async def fetch_all(self):
        """Fetch all data from the backend servers."""
        tasks = []

        async with ClientSession(auth=self._auth, headers=self._headers) as session:
            for url in ENDPOINTS:
                attr_override = ATTR_RECIPE_ITEMS if url == ATTR_RECIPES else None
                task = asyncio.ensure_future(_fetch(url, session, attr_override))
                tasks.append(task)

            fetch_results = await asyncio.gather(*tasks)
            self._process_responses(fetch_results)

            try:
                recipe_items = self.__getattribute__(ATTR_RECIPE_ITEMS)
                tasks = [asyncio.ensure_future(_fetch(RECIPE_ENDPOINT % recipe_item['uid'], session, ATTR_RECIPES)) for
                         recipe_item in recipe_items if recipe_item.get('uid', None)]
                fetch_results = await asyncio.gather(*tasks)
                self.__setattr__(ATTR_RECIPES, [result[KEY_RESPONSE] for result in fetch_results])
            except AttributeError:
                self.__setattr__(ATTR_RECIPES, [])

    def get_bookmarks(self):
        return self.__getattribute__('bookmarks')

    def get_categories(self):
        return self.__getattribute__('categories')

    def get_groceries(self):
        return self.__getattribute__('groceries')

    def get_meals(self):
        return self.__getattribute__('meals')

    def get_menus(self):
        return self.__getattribute__('menus')

    def get_menu_items(self):
        return self.__getattribute__('menuitems')

    def get_pantry_items(self):
        return self.__getattribute__('pantry')

    def get_recipes(self):
        return self.__getattribute__('recipes')

    def get_status(self):
        return self.__getattribute__('status')
