#tower.py
import checkinbetween as c
def move_tower(curr_pos,chessboard,next_pos):
   flag=False
   if curr_pos[0]==next_pos[0]:
       chessboard, flag=  c.checkinbetweenhorizontal(curr_pos,chessboard,next_pos)
   elif curr_pos[1]==next_pos[1]:
       chessboard, flag=c.checkinbetweenvertical(curr_pos,chessboard,next_pos)
   if flag:
	   chessboard[c.translate_position(next_pos)]=chessboard[c.translate_position(curr_pos)]
	   chessboard[c.translate_position(curr_pos)]='e'
   return chessboard, flag
   
