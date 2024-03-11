import asyncio
import sys

from pyrogram import *
from pyrogram.errors import *

from assistant import bot_plugins
from Mix import *


async def test():
    LOGGER.info(f"Check Updater...")
    await cek_updater()
    LOGGER.info(f"Updater Finished...")
    LOGGER.info(f"Connecting to {ndB.name}...")
    if ndB.ping():
        LOGGER.info(f"Connected to {ndB.name} Successfully!")
    try:
        LOGGER.info(f"Starting Telegram Client...")
        await user.start()
        await refresh_modules()
    except SessionExpired:
        LOGGER.info("Session Expired . Create New Session")
        sys.exit(1)
    except ApiIdInvalid:
        LOGGER.info("Api ID Not Valid.")
        sys.exit(1)
    except UserDeactivatedBan:
        LOGGER.info("Huahahahaha Akun Lu Ke Deak Cokk.")
        sys.exit(1)
    if bot_token is None:
        await autobot()
        await asyncio.sleep(1)
    try:
        await bot.start()
        await bot_plugins()
        await asyncio.sleep(1)
    except AccessTokenExpired:
        LOGGER.info("Token Expired.")
        sys.exit(1)
    except SessionRevoked:
        LOGGER.info("Token Revoked.")
        sys.exit(1)
    except AccessTokenInvalid:
        LOGGER.info("Token Invalid, Try again.")
        sys.exit(1)


async def main():
    await test()
    try:
        await refresh_cache()
        await check_logger()
        LOGGER.info(f"Check Finished.")
        LOGGER.info(f"Modules Imported...")
        LOGGER.info("Successfully Started Userbot.")
        await isFinish()
        await getFinish()
        if "test" not in sys.argv:
            await idle()
    except KeyboardInterrupt:
        LOGGER.warning("BOT STOP....")
    finally:
        await aiohttpsession.close()


if __name__ == "__main__":
    loop.run_until_complete(main())
