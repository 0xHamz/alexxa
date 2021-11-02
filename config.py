import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "AQBLOLeVv1W2LvAXQe9TrTT8U7do-TbSebjQ_rlCuJZWERJlodZjs0hcXbuJBMdB1bYHz67RNN4ywi62JwstYwqUTwlGqime0jjtbJ6UE-Q_N2YOdyQJGI_A2x_9MvD8Ru2j3cR3ER_bM4M-9NG4T-sZNcHTGxrCuI9ppvMTLrYzZ_2KWVAKTqp4gvwu-DTHhBLo2D16VvwzDQnFId-Z36YRiDVevokcohE9ubBsd9oYt-2HRH8Thw1g15hxLOEgtB1gZmT1vBc0pOXPFmRWxwLJR_r70-mGKXjwhQBb2RmWbyrT1GXvSAel1Eg8FeXXhxziB7lfMtSLm4LjUiczYXUgSW3WRQA")
BOT_TOKEN = getenv("BOT_TOKEN", "1858649461:AAELCYpz9xECqDcsjcCSDU3zNerx_6x88rY")
BOT_NAME = getenv("BOT_NAME", "𝐂𝐚𝐧𝐝𝐮𝐌𝐮𝐬𝐢𝐜𝐁𝐨𝐭")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "-1001319845035")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/41126266cb7db2240e798.png")
admins = {}
API_ID = int(getenv("API_ID", "3371945"))
API_HASH = getenv("API_HASH", "880695522786b34a4e943902db6e4f64")
BOT_USERNAME = getenv("BOT_USERNAME", "candumusic_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "robotassisten2")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "robotprojectx")
PROJECT_NAME = getenv("PROJECT_NAME", "𝐂𝐚𝐧𝐝𝐮𝐌𝐮𝐬𝐢𝐜𝐁𝐨𝐭")
OWNER = getenv("OWNER", "@justthetech")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/Vckyou/Geez-MusicProject")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "15"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1652454077").split()))
