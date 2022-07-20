
from pyrogram import Client , filters
from details import api_id, api_hash, bot_token
import tgcrypto

bot = Client("my bot",
            api_id = api_id,
            api_hash = api_hash,
            bot_token = bot_token)
@bot.on_message(filters.command(['start']) & filters.private)

def welcome(Client,message):
    message.reply_video(video="https://file2directlink.herokuapp.com/65068823684674195530940540/AgADCAUA/2_5350717343083272678.mp4")
bot.run()
