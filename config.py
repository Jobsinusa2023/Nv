#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5928843266:AAHe2UfiOUEWS-ni4LyTwV_9nsr7Wa3OlFc")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "29589634"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "7a5a583e0ca62896d9bcb0e5198faeba")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001501757058"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5452677687"))

#Port
PORT = os.environ.get("PORT", "80")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://filesend:filesend@cluster0.j8owkzx.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNELP = int(os.environ.get("FORCE_SUB_CHANNELP", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "100"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "ʜᴇʟʟᴏ, {first}\n\nᴛʜɪs ɪs ᴀ ᴘᴇʀᴍᴀɴᴇɴᴛ  ꜰɪʟᴇsᴛᴏʀᴇ ʙᴏᴛ .\n\nʜᴏᴡ ᴛᴏ ᴜsᴇ ʙᴏᴛ ɪᴛ's ʙᴇɴᴇꜰɪᴛs??\n\n📢 sᴇɴᴅ ᴍᴇ ᴀɴʏ ꜰɪʟᴇ & ɪᴛ ᴡɪʟʟ ʙᴇ ᴜᴘʟᴏᴀᴅᴇᴅ ɪɴ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ & ʏᴏᴜ ᴡɪʟʟ ɢᴇᴛ ᴛʜᴇ ꜰɪʟᴇ ʟɪɴᴋ.\n\n⚠️ ʙᴇɴᴇꜰɪᴛs: ɪꜰ ʏᴏᴜ ʜᴀᴠᴇ ᴀ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴏᴠɪᴇ ᴄʜᴀɴɴᴇʟ ᴏʀ ᴀɴʏ ᴄᴏᴘʏʀɪɢʜᴛ ᴄʜᴀɴɴᴇʟ, ᴛʜᴇɴ ɪᴛs ᴜsᴇꜰᴜʟ ꜰᴏʀ ᴅᴀɪʟʏ ᴜsᴀɢᴇ, ʏᴏᴜ ᴄᴀɴ sᴇɴᴅ ᴍᴇ ʏᴏᴜʀ ꜰɪʟᴇ & ɪ ᴡɪʟʟ sᴇɴᴅ ᴘᴇʀᴍᴀɴᴇɴᴛ ʟɪɴᴋ ᴛᴏ ʏᴏᴜ & ᴄʜᴀɴɴᴇʟ ᴡɪʟʟ ʙᴇ sᴀꜰᴇ ꜰʀᴏᴍ ᴄᴏᴘʏʀɪɢʜᴛ ɪɴꜰʀɪɴɢᴇᴍᴇɴᴛ ɪssᴜᴇ.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5452677687").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my both 2 Channels to use me\n\nKindly Please join both 2 Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

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
