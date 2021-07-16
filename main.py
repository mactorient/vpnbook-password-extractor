# ------------------------------------------------
# * Created by github.com/mactorient
# * This tool gets pptp vpn password from vpnbook
# ------------------------------------------------

try:
    from pyperclip import copy as copy_to_clipboard
    from pytesseract import image_to_string as ocr # To extract the password from the photo
    from PIL import Image
    import requests
    import tempfile
except ImportError as e:
    print("[ERROR] Import Error:", e)
    quit(0)

def get_password():
    global PASSWORD
    TEMP_FILE= tempfile.NamedTemporaryFile(mode='r+', suffix='.png').name
    URL= 'https://www.vpnbook.com/password.php'

    IMAGE_DATA= requests.get(URL).content
    with open(TEMP_FILE, 'wb') as file: file.write(IMAGE_DATA)
    
    IMAGE= Image.open(TEMP_FILE)
    PASSWORD= ocr(IMAGE).replace('\n', '')
    
    return PASSWORD


def main():
    try: 
        password= get_password()
        print("[SYSTEM] PPTP Password: %s" % password)
    except Exception as e:
        print('[ERROR] Something went wrong:', e)
    else:
        copy = input("[SYSTEM] Do you want to copy password to clipboard? (y/n): ")
        if copy.strip().lower()=="y":
            copy_to_clipboard(password)
            print("[CLIPBOARD] Copied: %s" % password)


if __name__=='__main__':
    main()