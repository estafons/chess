#chess_server.py

import socket
import random
from make_move import make_move
chessboard = ['T','H','B','Q','K','B','H','T','P','P','P','P','P','P','P','P','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','p','p','p','p','p','p','p','p','t','h','b','q','k','b','h','t']
def initialize():
    turn = random.randint(0, 1) #both players select 1 or 0 at start (must be different) if they get it they start first. perform a mod 2 to check whos turn is it every time
    
    
def print_chessboard(chessboard):
    i=0
    for x in chessboard:
       i=i+1
       print(x+' ', end= '')
       if i%8==0:
          print('\n')

initialize()
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
   s.bind((HOST, PORT))
   s.listen()
   while True:
       conn, addr = s.accept()	 
       data = conn.recv(1024)
       data= data.decode('utf-8')
       curr_pos=data[:2]
       next_pos=data[2:4]
       #try:
       chessboard,flag=make_move(curr_pos,chessboard,next_pos)
       #   break
       #except TypeError:
        #  print("we had an error")
       board=''.join(chessboard)
       conn.sendall(board.encode('utf-8'))
    
     

