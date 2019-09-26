#chess_client.py

import socket
import time
def print_chessboard(chessboard):
    i=0
    for x in chessboard:
       i=i+1
       print(x+'   ', end= '')
       if i%8==0:
          print('\n')
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server
while True:
   move=str(input("give me desired move"))
   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:	
     s.connect((HOST, PORT))
     s.sendall(move.encode('utf-8'))
     data = s.recv(1024)
     data= data.decode('utf-8')
     print_chessboard(list(data))
