#queen.py
import checkinbetween as c
def move_queen(curr_pos,chessboard,next_pos):
   flag=False
   if abs(int(curr_pos[1])-int(next_pos[1]))==abs(ord(curr_pos[0])-ord(next_pos[0])): #move is valid (diagonal)
	   chessboard, flag = c.checkinbetween_diagonal(curr_pos,chessboard,next_pos)
   elif curr_pos[0]==next_pos[0]:
       chessboard, flag=  c.checkinbetweenhorizontal(curr_pos,chessboard,next_pos)
   elif curr_pos[1]==next_pos[1]:
       chessboard, flag=c.checkinbetweenvertical(curr_pos,chessboard,next_pos)
   if flag:
	   chessboard[c.translate_position(next_pos)]=chessboard[c.translate_position(curr_pos)]
	   chessboard[c.translate_position(curr_pos)]='e'
   return chessboard, flag
