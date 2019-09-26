#pawn.py
import checkinbetween as c
def move_pawn(curr_pos,chessboard,next_pos):
   valid_move=False
   if curr_pos[0]==next_pos[0]:
       if (abs(int(curr_pos[1])-int(next_pos[1]))==2):
          chessboard, valid_move= c.checkinbetweenhorizontal(curr_pos,chessboard,next_pos)
       elif abs(int(curr_pos[1])-int(next_pos[1]))==1:
          chessboard, valid_move= c.checkinbetweenhorizontal(curr_pos,chessboard,next_pos)
       elif (abs(int(curr_pos[1])-int(next_pos[1]))==1)and (ord(cur_pos[0]-next_pos[0])): 
          y=c.translate_position(next_pos)
          if chessboard[y]!='e':
              valid_move=True
   if valid_move:
       chessboard[c.translate_position(next_pos)]=chessboard[c.translate_position(curr_pos)]
       chessboard[c.translate_position(curr_pos)]='e'
   return chessboard, valid_move
