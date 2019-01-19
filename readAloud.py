import ocr
import jtalk
import subprocess
import tkinter
from tkinter import filedialog as tkFileDialog
   
root = tkinter.Tk()
root.withdraw()
   
fType = [('pngファイル','*.png')]
iDir = '/'

filename = tkFileDialog.askopenfilename(filetypes=fType,initialdir=iDir)

def main():
  img_base64 = ocr.img_to_base64(filename)
  result = ocr.request_cloud_vison_api(img_base64)
  text_r = result["responses"][0]["fullTextAnnotation"]["text"]
  jtalk.run(text_r.replace('\n',' '))
  
  cmd = ['open','voice.wav']
  r = subprocess.run(cmd)
  print(r)
  print(text_r)

  
if __name__ == "__main__":
    main()  
