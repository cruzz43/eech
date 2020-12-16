import os

# DO NOT EDIT THIS FILE
# DO NOT EDIT THIS FILE
# DO NOT EDIT THIS FILE
# DO NOT EDIT THIS FILE

# READ README FOR CONFIG


class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1298877553:AAH96o8RNrl3z51YiykTJp6HfVJHrf8Tpks")
    # The Telegram API things
    APP_ID = int(os.environ.get("APP_ID", "1517192"))
    API_HASH = os.environ.get("API_HASH", "d522013bbca2d46e256145b13f967aee")
    OWNER_ID = int(os.environ.get("OWNER_ID", "885488992"))
    # Get these values from my.telegram.org
    # to store the channel ID who are authorized to use the bot
    AUTH_CHANNEL = set(int(x) for x in os.environ.get("AUTH_CHANNEL", "-1001267728460,891835214,445083284").split(","))
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    #
    ARIA_TWO_STARTED_PORT = int(os.environ.get("ARIA_TWO_STARTED_PORT", 6800))
    EDIT_SLEEP_TIME_OUT = int(os.environ.get("EDIT_SLEEP_TIME_OUT", 15))
    MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START = int(os.environ.get("MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START", 600))
    MAX_TG_SPLIT_FILE_SIZE = int(os.environ.get("MAX_TG_SPLIT_FILE_SIZE", 1072864000))
    # add config vars for the display progress
    FINISHED_PROGRESS_STR = os.environ.get("FINISHED_PROGRESS_STR", "█")
    UN_FINISHED_PROGRESS_STR = os.environ.get("UN_FINISHED_PROGRESS_STR", "░")
    # add offensive API
    TG_OFFENSIVE_API = os.environ.get("TG_OFFENSIVE_API", None)
    CUSTOM_FILE_NAME = os.environ.get("CUSTOM_FILE_NAME", "")
    LEECH_COMMAND = os.environ.get("LEECH_COMMAND", "leech@tleeechbot")
    YTDL_COMMAND = os.environ.get("YTDL_COMMAND", "ytdl@tleeechbot")
    RCLONE_CONFIG = os.environ.get("RCLONE_CONFIG", """type = drive
client_id = 1031701960500-dvlfkduk2lf7gs45h9nctc6thnldlm65.apps.googleusercontent.com
client_secret = edpe9ohGkBtLfOr3OP8geJcN
scope = drive
root_folder_id =
token = {"access_token":"ya29.A0AfH6SMATXX-94OigVOiDBBLfGfsKj_WtqYaGq05qUsUcu4LkTrGQqLdpZc2di4-cNVF9N6NHArVAJn2pYhnqc-rO8nXZlWnQDdUoLIBjlKDEfbiKJvD01ZY99M8VtkyBUMWpa-B1a4kMi3S0JeubZHxvn6V7ExPu8MZSd2q076Y","token_type":"Bearer","refresh_token":"1//0grla1g7cLI88CgYIARAAGBASNwF-L9IrE0iHQ68eEmhGlsT5mQl5Ii-Mm4IqB-hCNe44fczi6aosrRlG8E2dG-z8rx1INp4_5vE","expiry":"2020-10-20T18:34:46.8879996Z"}
team_drive = 0APEaD85l8G7CUk9PVA""")
    DESTINATION_FOLDER = os.environ.get("DESTINATION_FOLDER", "ALLINONE")
    GLEECH_COMMAND = os.environ.get("GLEECH_COMMAND", "gleech@tleeechbot")
    INDEX_LINK = os.environ.get("INDEX_LINK", "https://drake.dewitt.workers.dev/ALLINONE")
    TELEGRAM_LEECH_COMMAND_G = os.environ.get("TELEGRAM_LEECH_COMMAND_G", "tleech@tleeechbot")
    CANCEL_COMMAND_G = os.environ.get("CANCEL_COMMAND_G", "cancel")
    GET_SIZE_G = os.environ.get("GET_SIZE_G", "getsize@tleeechbot")
    STATUS_COMMAND = os.environ.get("STATUS_COMMAND", "status@tleeechbot")
    SAVE_THUMBNAIL = os.environ.get("SAVE_THUMBNAIL", "savethumbnail")
    CLEAR_THUMBNAIL = os.environ.get("CLEAR_THUMBNAIL", "clearthumbnail")
    UPLOAD_AS_DOC = os.environ.get("UPLOAD_AS_DOC", "False")
    PYTDL_COMMAND_G = os.environ.get("PYTDL_COMMAND_G", "pytdl@tleeechbot")
    LOG_COMMAND = os.environ.get("LOG_COMMAND", "log")
    CLONE_COMMAND_G = os.environ.get("CLONE_COMMAND_G", "gclone")
    UPLOAD_COMMAND = os.environ.get("UPLOAD_COMMAND", "upload")
    RENEWME_COMMAND = os.environ.get("RENEWME_COMMAND", "renewme@tleeechbot")
