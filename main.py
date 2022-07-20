
from pyrogram import Client , filters
from details import api_id, api_hash, bot_token
import tgcrypto
import requests
import os
import time

bot = Client("my bot",
            api_id = api_id,
            api_hash = api_hash,
            bot_token = bot_token)
@bot.on_message(filters.command(['start']) & filters.private)

def welcome(Client,message):
    url = "https://file2directlink.herokuapp.com/65068823684674195530940540/AgADCAUA/2_5350717343083272678.mp4"
    download(url)
    print("im from end")
    message.reply_video(video="2_5350717343083272678.mp4")

    file_name  = url.split("/")[-1]
    os.remove(file_name)
    print("endd")
def download(url):
    get_response = requests.get(url,stream=True)
    file_name  = url.split("/")[-1]
    with open(file_name, 'wb') as f:
        for chunk in get_response.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
    
    print(file_name)
    return file_name

            
bot.run()
