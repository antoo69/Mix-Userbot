from os import getenv

from dotenv import load_dotenv

load_dotenv()

api_id = int(getenv("api_id", None))
api_hash = getenv("api_hash", None)
session = getenv("session", None)
bot_token = getenv("bot_token", "7521665419:AAG3d0qbg1v4-vGpiJLDY8N_ecQpsD6Kwx0")
db_name = getenv("db_name", None)
mongo_uri = getenv("mongo_uri", None)
def_bahasa = getenv("def_bahasa", "toxic")
log_pic = getenv("log_pic", "https://telegra.ph/file/a23e9cf302c1da667bd89.jpg")
heroku_api = getenv("heroku_api")
heroku_app_name = getenv("heroku_app_name")
ADMIN_IDS = list(map(int, os.getenv("ADMIN_IDS", "7083782157").split(',')))
upstream_repo = getenv(
    "upstream_repo",
    "https://github.com/antoo69/F-Userbot",
)
upstream_branch = getenv("upstream_branch", "final")
git_token = getenv("git_token", None)
log_channel = getenv("log_channel", None)
genius_api = getenv(
    "genius_api",
    "zhtfIphjnawHBcLFkIi-zE7tp8B9kJqY3xGnz_BlzQM9nhJJrD7csS1upSxUE0OMmiP3c7lgabJcRaB0hwViow",
)
# scheme = getenv("scheme", None)
# hostname = getenv("hostname", None)
# port = int(getenv("port", None))
# username = getenv("username", None)
# password = getenv("password", None)
