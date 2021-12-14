import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = (environ.get('PICS', 'https://telegra.ph/file/b4de33f0d9522c573d934.jpg https://telegra.ph/file/7364231d55706049ac926.jpg https://telegra.ph/file/fbaeb961e2f5a9437c2ba.jpg https://telegra.ph/file/0e565e92e3d8b82836c96.jpg https://telegra.ph/file/b4507f3e87e01241f0754.jpg https://telegra.ph/file/594a1c60c884cffc18ff0.jpg https://telegra.ph/file/846be1e02773e7eb600df.jpg https://telegra.ph/file/039f2a526a11bac1cb82f.jpg https://telegra.ph/file/cf77eba0cb06d16670738.jpg https://telegra.ph/file/ad786fb34664d64636d6d.jpg https://telegra.ph/file/46a949c1de9e361be9c1f.jpg https://telegra.ph/file/366f244f13a45ef35d8e1.jpg https://telegra.ph/file/af8ea2e1f5ee9188413c4.jpg https://telegra.ph/file/f60b89789b2b718d792cb.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "tgmoviebot")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', 0))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'Rudster_Modz')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "<code>{file_name}</code>\n\n<b>Size:</b> {file_size}\n\n<b>Join [Jos Movie Club](https://t.me/kotacinemamall) for more Movies </b>")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>🎬 Title:</b> <a href={url}>{title}</a>\n<b>📺 Type:</b> {kind}\n<b>📆 Release:</b> <a href={url}/releaseinfo>{release_date}</a>\n<b>🌟 Rating:</b> <a href={url}/ratings>{rating} / 10</a>\n(based on <code>{votes}</code> user ratings.)\n\n<b>📀 Runtime:</b> <code>{runtime} minutes</code>\n<b>🎭 Genres:</b> {genres}\n\n<b>☀️ Languages:</b> {languages}\n<b>🎛 Countries:</b> {countries}\n<b>🎥 Director:</b> {director}\n<b>📝 Writers:</b> {writer}\n\n<b><a href='https://t.me/kotacinemamall'>Ⓒ {message.chat.title}</a></b>\n\n<b>✍️ Note:</b> <s>This message will be Auto-deleted after 5 minutes to avoid copyright issues.</s>")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two seperate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as diffrent buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your Currect IMDB template is {IMDB_TEMPLATE}"
