import asyncio
import logging

from pyprika.data.paprika_client import PaprikaClient

_LOGGER = logging.getLogger(__name__)


async def main():
    client = PaprikaClient("alan.janis@gmail.com", "}Jj8c2uWNV{3uTc+XAFB")
    await client.fetch_all()
    _LOGGER.warning("{}".format(client.get_groceries()))


if __name__ == __name__:
    _ = asyncio.get_event_loop().run_until_complete(main())
