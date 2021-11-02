import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQBoSzVD_FSY5sHW3Z43_4C9YkileACmxJyKu35sHrfUTsoFnAor6Xp3rBBRkhUAmntes7YpWOVcg91t7UMQQ8JheLV96cKrL7rEP8kIj9zShfv7Xod6n-Pha4-X5M8072SSqtLf1monhZTF78fh1Sht67zZtVl_nbCmlNBg0ofiGGqrWhtgsU_wqDvrdNVCesggw5h0HYDvmcrLN5W5qJMRhNKReHvo2bhkR0KRJ8GRpifsYK2qtKJiKcE_yoNZLk8gP0T4FwMDc3h2t3mxHYjfv_O7cMLPhSeOyhAsh1iMCFzvpIheuecyCd7N-YZ6Sge5l5j4z7scZqMZFd--Yz8baT9o4gA")
BOT_TOKEN = getenv("BOT_TOKEN", "2072190749:AAENijOi3p9CxSoJeDrKkWRPb_KziRuJNVM")
BOT_NAME = getenv("BOT_NAME", "Alexa")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "-1001319845035")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/36256d986b9c69902e4c4.png")
admins = {}
API_ID = int(getenv("API_ID", "6847114"))
API_HASH = getenv("API_HASH", "7f2c9b9ac20e6840d13f9ca85e1c4e2d")
BOT_USERNAME = getenv("BOT_USERNAME", "alexagroup_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "alexaassisten")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "robotprojectx")
PROJECT_NAME = getenv("PROJECT_NAME", "Alexa")
DATABASE_URL = os.environ.get("mongodb+srv://alexam:sad1899@cluster0.f5kx3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
OWNER = getenv("OWNER", "justthetech")
OWNER_NAME=justthetech
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/Vckyou/Geez-MusicProject")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "15"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "927625147").split()))
