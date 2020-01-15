import asyncio
import logging

from timeit import default_timer

import async_timeout
from aiohttp import BasicAuth, ClientSession
from aiohttp.hdrs import USER_AGENT, ACCEPT

from .models.bookmark import Bookmark
from .models.category import Category
from .models.grocery_item import GroceryItem
from .models.meal import Meal
from .models.menu import Menu
from .models.menu_item import MenuItem
from .models.pantry_item import PantryItem
from .models.recipe_item import RecipeItem
from .models.status import Status
from ..const import CLIENT_USER_AGENT, APPLICATION_JSON, BASE_URL

_LOGGER = logging.getLogger(__name__)

KEY_RESPONSE = 'resp'
KEY_URL = 'url'
KEY_ELAPSED = 'elapsed'

ENDPOINTS = {
    'bookmarks': Bookmark,
    'categories': Category,
    'groceries': GroceryItem,
    'meals': Meal,
    'menus': Menu,
    'menuitems': MenuItem,
    'pantry': PantryItem,
    'recipes': RecipeItem,
    'status': Status
}


async def fetch(url, session):
    """ Fetch a single URL """
    with async_timeout.timeout(10):
        async with session.get("%s/%s" % (BASE_URL, url)) as response:
            before_request = default_timer()
            resp = await response.json()
            elapsed = default_timer() - before_request

            _LOGGER.debug(
                "URL {} took {}",
                url,
                elapsed
            )

            return {
                KEY_RESPONSE: resp,
                KEY_URL: url,
                KEY_ELAPSED: elapsed
            }


class PaprikaClient:
    """Client to connect to Paprika backend servers."""

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
            url = result[KEY_URL]
            response = result[KEY_RESPONSE]
            model_class = ENDPOINTS[url]




    async def fetch_all(self):
        """Fetch all data from the backend servers."""
        tasks = []

        async with ClientSession(auth=self._auth, headers=self._headers) as session:
            for url in list(ENDPOINTS.keys()):
                task = asyncio.ensure_future(fetch(url, session))
                tasks.append(task)

            fetch_results = await asyncio.gather(*tasks)
