# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @UcCarding_World
# Backup Channel @BiryaniTeam
# Developer @Space_Carder




import os
import logging
from logging.handlers import RotatingFileHandler




TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
APP_ID = int(os.environ.get("APP_ID", "21346742"))
API_HASH = os.environ.get("API_HASH", "571dd0607522052217b398aa3cd860d8")


OWNER = os.environ.get("OWNER", "Space_Carder") #Owner username
OWNER_ID = int(os.environ.get("OWNER_ID", "1345506970")) #Owner user id
DB_URL = os.environ.get("DB_URL", "mongodb+srv://VEGBIRYANI:VEGBIRYANI@sexyvegbriyani.b1zse.mongodb.net/?retryWrites=true&w=majority&appName=SexyVegBriyani")
DB_NAME = os.environ.get("DB_NAME", "sexybiryani")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002037458506"))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002124699670"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1001996096940"))


SECONDS = int(os.getenv("SECONDS", "600")) # auto delete in seconds



PORT = os.environ.get("PORT", "8083")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "100"))




START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in G SHIT Channel and other users can access it from special link.")

try:
    ADMINS=[7085541484]
    for x in (os.environ.get("ADMINS", "1345506970").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")


FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly i only work for my respected admin ji!"

ADMINS.append(OWNER_ID)
ADMINS.append(1345506970)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @UcCarding_World
# Backup Channel @BiryaniTeam
# Developer @Space_Carder
