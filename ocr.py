import requests
import base64
import json
"""
import tkinter 
from tkinter import messagebox as tkMessageBox 
from tkinter import filedialog as tkFileDialog 

root = tkinter.Tk()
root.withdraw()

fType = [('pngファイル','*.png')]
iDir = '/'

filename = tkFileDialog.askopenfilename(filetypes=fType,initialdir=iDir)
"""
GOOGLE_CLOUD_VISION_API_URL = 'https://vision.googleapis.com/v1/images:annotate?key='
API_KEY = 'AIzaSyD_WcA55b6MsIR45q1puR3OzyVqaoAlEu4' 

def request_cloud_vison_api(image_base64):
    api_url = GOOGLE_CLOUD_VISION_API_URL + API_KEY
    req_body = json.dumps({
        'requests': [{
            'image': {
                'content': image_base64.decode('utf-8') 
            },
            'features': [{
                'type': 'TEXT_DETECTION', 
                'maxResults': 10,
            }]
        }]
    })
    res = requests.post(api_url, data=req_body)
    return res.json()

# 画像読み込み
def img_to_base64(filepath):
    with open(filepath, 'rb') as img:
        img_byte = img.read()
    return base64.b64encode(img_byte)
"""
def main():
  img_base64 = img_to_base64(filename)
  result = request_cloud_vison_api(img_base64)
  #print("{}".format(json.dumps(result, indent=4)))
  text_r = result["responses"][0]["fullTextAnnotation"]["text"]
  #print(text_r)
"""
#print("AAAAAA")

if __name__ == "__main__":
  main()
