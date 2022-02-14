import socket, time
from PIL import Image

# SERVER = '3.138.180.119' #127.0.0.1
# PORT = 18043
SERVER = 'localhost'
PORT = 5454


client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((SERVER,PORT))
print(f"[CONNECTED] Connected to {SERVER}:{PORT}")

def SendImage():
    file = 'Image-Path'
    print(f'[PROCESSING] Sending {file}...')
    
    with open(file, 'rb') as f:
        data = f.read()
    client.send(str(len(data)).encode())
    time.sleep(3)
    client.send(data)    

    print(f'[FILE SENT] Image Sended to {SERVER}...')
    # Image.open(file).show()
    # im.close()

SendImage()