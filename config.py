import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 25852103
API_HASH = "aaf98935d7ab5b0bae397e12358cc848"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7029503067:AAGH5RVfHrOYTJgpTrms5ZD3MxUZwAtmnBI"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://timepass2000009:timepass2000009@cluster0.zh8kd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = -1002431719503

# Get this value from @ultron2_robot on Telegram by /id
OWNER_ID = 6839247258

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/rishabhops/alice",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = "https://t.me/crunchyroll_anime_in_hindi_32"
SUPPORT_GROUP = "https://t.me/ANIME_HINDI_HUB_32"

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "BQGKeMcAHYmz9q0RaIlCuk_3P7k4gS7fB1aEqyI2Ar3g_ta3b7dAJ6sotf4ExNwdkFGJ9A0qmJ8eO_NqxOJVg8MpaDd8NkGimH18gK1dbP2_T9eoyTocZK5ejOh2tloH6pz8XOWC-tKkB42k_IbeAqsbH5jgeVf11q_ZPisz5klHZgEAzLXtKpJ6wgJre3kHWyQStzmXa6rZWKmn0CxlBI3S820Y-FAmcBPjCL9mALKpT0iNqlRMw4egsOxnv5ynnIOS0qkGPcCccTHjntqVTKGYYkYZeA4L8kjUqWgrKCt-c8loHcZ34ctUIHpdKd5lJqI2AjqxRB3P-OB3duUSpCDnWR7ySgAAAAGXpqGaAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = "https://graph.org/file/1b39f6fb268a2467e7062-b74f21344292eb5889.jpg"

PING_IMG_URL = "https://graph.org/file/1b39f6fb268a2467e7062-b74f21344292eb5889.jpg"

PLAYLIST_IMG_URL = "https://graph.org/file/1b39f6fb268a2467e7062-b74f21344292eb5889.jpg"
STATS_IMG_URL = "https://graph.org/file/1b39f6fb268a2467e7062-b74f21344292eb5889.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/1b39f6fb268a2467e7062-b74f21344292eb5889.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/1b39f6fb268a2467e7062-b74f21344292eb5889.jpg"
STREAM_IMG_URL = "https://graph.org/file/1b39f6fb268a2467e7062-b74f21344292eb5889.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/1b39f6fb268a2467e7062-b74f21344292eb5889.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/1b39f6fb268a2467e7062-b74f21344292eb5889.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/1b39f6fb268a2467e7062-b74f21344292eb5889.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/1b39f6fb268a2467e7062-b74f21344292eb5889.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/1b39f6fb268a2467e7062-b74f21344292eb5889.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
