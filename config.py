import os

APP_HASH= "be7b1d39ac5116d22701f8b6ac956785"
BOT_TOKEN= "5255621390:AAEiWNN3Zy1BISUj2PhYnlVulR2emKDGYhA"
SESSION_NAME= "zipfile_bot"
bot_token=os.getenv("BOT_TOKEN")
app_id=int(os.getenv("APP_ID", 4926633))
app_hash=os.getenv("APP_HASH")
session_dsn=os.getenv("SESSION_NAME")
