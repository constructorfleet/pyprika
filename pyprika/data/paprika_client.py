import asyncio
from aiohttp import BasicAuth, ClientSession
from .models.bookmark import Bookmark
from .models.category import Category
from .models.grocery_item import GroceryItem

ENDPOINTS = {
    'bookmarks': Bookmark,
    'categories': Category,
    'groceries': GroceryItem,
    'meals': Meal
}


class PaprikaClient:
    """Client to connect to Paprika backend servers."""

    def __init__(self, username, password):
        """Initialize the client."""
        self._auth = BasicAuth(
            login=username,
            password=password
        )

    async def fetch_all(self):
        """Fetch all data from the backend servers."""
        async with ClientSession(headers=custom_headers) as session:
            for url in urls:
                task = asyncio.ensure_future(fetch(url, session))
                tasks.append(task)

            _ = await asyncio.gather(*tasks)
