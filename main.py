
from pyrogram import Client , filters
from details import api_id, api_hash, bot_token
import tgcrypto
import requests
import os
import time
from urllib.parse import urlparse

bot = Client("my bot",
            api_id = api_id,
            api_hash = api_hash,
            bot_token = bot_token)
@bot.on_message(filters.command(['start']) & filters.private)

def welcome(Client,message):
    message.reply_text(text="hi")
    url = "https://file2directlink.herokuapp.com/65686715824167183548198464/AgADtiEA/Bhool.Bhulaiyaa.2.2022.PreDvd.Hindi.480p_mkvCinemas.mkv"

    file_name  = download(url)
    #url = "https://file2directlink.herokuapp.com/65068823684674195530940540/AgADCAUA/2_5350717343083272678.mp4"
    download(url)
    print("im from end")
    message.reply_video(file_name)

    
    #os.remove(file_name)
    print("endd")

def download(url):
    a = urlparse(url)
    print(a.path)
    file_name = os.path.basename(a.path)

  
    get_response = requests.get(url,stream=True)
    #f#le_name  = url.split("/")[-1]
    with open(file_name, 'wb') as f:
        for chunk in get_response.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
    return file_name


            
bot.run()
