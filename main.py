# ------------------------------------------------
# * Created by github.com/mactorient
# ? This tool gets pptp vpn password from vpnbook
# ------------------------------------------------

from pyperclip import copy as copy_to_clipboard
from pytesseract import image_to_string as ocr # for requested
from PIL import Image
import requests
import tempfile

def get_password():
    _file= tempfile.NamedTemporaryFile(mode='r+', prefix='vpnbook_', suffix='.png').name
    img_url= 'https://www.vpnbook.com/password.php'
    img_data= requests.get(img_url).content
    with open(_file, 'wb') as f:
        f.write(img_data)
    _password= ocr(Image.open(_file)).replace('\n', '')
    return _password

def main():
    try: 
        password= get_password()
        copy_to_clipboard(password)
        print('Password copied to clipboard: {}'.format(password))
    except Exception as e: print('Something went wrong:', e)

if __name__=='__main__':
    main()