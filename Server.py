import socket
from PIL import Image

SERVER = 'localhost'
PORT = 5454

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((SERVER,PORT))
print(f"[LISTENING] Server is listening on {SERVER}:{PORT}")


server.listen(1)
conn, addr = server.accept()
print(f"[NEW CONNECTION] {conn} : {addr} connected.\n")

def ReceivePic(filename):
    size = conn.recv(1024).decode()
    data = conn.recv(int(size))  
    # print(size,len(data))
    with open(filename+'.png','wb') as f:
        f.write(data)
        
    print(f'[RECIEVED] Image file - {filename} Received Successfully..\n')        
    Image.open(filename+'.png').show()
    conn.close()

ReceivePic('ArcReactor1')    