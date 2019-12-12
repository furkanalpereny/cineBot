import requests
import shutil
import json
import os


def saveImage(link, path):
    if not os.path.exists(path):
        os.makedirs(path)

    image_url = link
    resp = requests.get(image_url, stream=True) #link requestile get edildi

    img_id = image_url.split("/pictures/")[-1] #link split edilerek son elemanı [-1] ile çekildi
    img_id = img_id.replace("/", "-")

    img_path = path + img_id
    local_file = open(img_path, 'wb')

    resp.raw.decode_content = True
    shutil.copyfileobj(resp.raw, local_file) #resim uzantısı belirtilen yere oluşturuldu
    print(img_path, "has downloaded successfully.")
    del resp

    return img_path
