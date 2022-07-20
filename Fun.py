import os,requests
def download(url):
    get_response = requests.get(url,stream=True)
    file_name  = url.split("/")[-1]
    with open(file_name, 'wb') as f:
        for chunk in get_response.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
    
    print(file_name)
    return file_name


#download("https://file2directlink.herokuapp.com/65068823684674195530940540/AgADCAUA/2_5350717343083272678.mp4")
