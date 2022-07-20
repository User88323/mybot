
from pyrogram import Client , filters
from details import api_id, api_hash, bot_token
import tgcrypto

bot = Client("my bot",
            api_id = int(os.environ["API_ID"]),
            api_hash = os.environ["API_HASH"],
            bot_token = os.environ["BOT_TOKEN"])
@bot.on_message(filters.command(['start']) & filters.private)

def welcome(Client,message):
    message.reply_video(video="2_5350717343083272678.mp4")
bot.run()
