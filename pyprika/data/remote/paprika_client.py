"""Client for communicating with the Paprika servers."""
import asyncio
import json
import logging
from timeit import default_timer

import async_timeout
from aiohttp import BasicAuth, ClientSession
from aiohttp.hdrs import USER_AGENT, ACCEPT, AUTHORIZATION

from pyprika.const import CLIENT_USER_AGENT, APPLICATION_JSON, BASE_URL

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


async def _fetch(auth, headers, url, session, attr_override=None):
    """Fetch a single URL """
    end_point = url if url.endswith('/') else (url + '/')
    uri = "%s%s" % (BASE_URL, end_point)
    with async_timeout.timeout(10):
        async with session.get(
                uri,
                auth=auth,
                headers=headers,
                allow_redirects=True) as response:
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

    def __init__(self, username, password):
        """Initialize the client."""
        self._auth = BasicAuth(username, password)
        self._headers = {
            USER_AGENT: CLIENT_USER_AGENT,
            ACCEPT: APPLICATION_JSON,
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
                task = asyncio.ensure_future(
                    _fetch(
                        self._auth,
                        self._headers,
                        url,
                        session,
                        attr_override
                    )
                )
                tasks.append(task)
            fetch_results = await asyncio.gather(*tasks)
            self._process_responses(fetch_results)

            self.__setattr__(ATTR_RECIPES, [])
            try:
                recipe_items = self.__getattribute__(ATTR_RECIPE_ITEMS)
                if not recipe_items:
                    return
                tasks = [asyncio.ensure_future(
                    _fetch(
                        self._auth,
                        self._headers,
                        RECIPE_ENDPOINT % recipe_item['uid'],
                        session,
                        ATTR_RECIPES
                    )) for recipe_item in recipe_items if recipe_item.get('uid', None)]
                fetch_results = await asyncio.gather(*tasks)
                self.__setattr__(ATTR_RECIPES, [result[KEY_RESPONSE] for result in fetch_results])
            except Exception as err:
                _LOGGER.error(str(err))

    def get_bookmarks(self):
        """Get bookmark json resources."""
        return self.__getattribute__('bookmarks') or []

    def get_categories(self):
        """Get category json resources."""
        return self.__getattribute__('categories') or []

    def get_groceries(self):
        """Get grocery json resources."""
        return self.__getattribute__('groceries') or []

    def get_meals(self):
        """Get meal json resources."""
        return self.__getattribute__('meals') or []

    def get_menus(self):
        """Get menu json resources."""
        return self.__getattribute__('menus') or []

    def get_menu_items(self):
        """Get menu item json resources."""
        return self.__getattribute__('menuitems') or []

    def get_pantry_items(self):
        """Get pantry item json resources."""
        return self.__getattribute__('pantry') or []

    def get_recipes(self):
        """Get recipes json resources."""
        return self.__getattribute__('recipes') or []

    def get_status(self):
        """Get recipe book status json resources."""
        return self.__getattribute__('status') or {}
