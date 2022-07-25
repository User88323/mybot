
from pyrogram import Client , filters
from details import api_id, api_hash, bot_token
import tgcrypto
import requests
import os
import time
from urllib.parse import urlparse
from bs4 import BeautifulSoup

bot = Client("my bot",
            api_id = api_id,
            api_hash = api_hash,
            bot_token = bot_token)
@bot.on_message(filters.command(['start']) & filters.private)

def welcome(Client,message):
    message.reply_text(text="hi?")
    
    url = "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ElephantsDream.mp4"


    a = urlparse(url)
    print(a.path)
    file_namex = os.path.basename(a.path)


    #url = "https://file2directlink.herokuapp.com/65527557316299204660527228/AgADtiEA/Bhool.Bhulaiyaa.2.2022.PreDvd.Hindi.480p_mkvCinemas.mkv"
    
    file_name  = url.split("/")[-1]
    print(file_name)
    download(url)
    #file_name1 = download(url)
    #download(url)
    print("iim from end")
    message.reply_video(file_namex)
    
    os.remove(file_namex)
    print("endd")
def download(url):
    a = urlparse(url)
    print(a.path)
    file_name1 = os.path.basename(a.path)


    get_response = requests.get(url,stream=True)
    file_name  = url.split("/")[-1]
    with open(file_name, 'wb') as f:
        for chunk in get_response.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
    
    print(file_name1)
def fetcher(pagel):
    pagel = "https://ok./sites/realitykings/"
    r = requests.get(bawal[i])
    html = r.content
    soup = BeautifulSoup(html,'html.parser')
    	
    ancr = soup.find_all('a')
    output = []
    lod = 0
    for link in ancr:
    	if (link.get('href').find("/video/") != -1):
            link = "https://ok.xxx/"+link.get('href')
            r = requests.get(link)
            source2 = r.content
            soup2 = BeautifulSoup(source2,'html.parser')
            div = soup2. find("a", {"class": "download-link"})
            cn = str(div)
            direct_l = cn[cn.find("http") : cn.find("style") - 2]
            output.append(direct_l)
            #update.message.reply_text(direct_l+"                          "+"Original_Link: "+link)
            lod = lod +1 
            print('____----______--- ' + str(lod) + '---_____---_____')
            print("\033c")
    return direct_l
            
bot.run()
