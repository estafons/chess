#knight.py
import checkinbetween as c

def move_knight(curr_pos,chessboard,next_pos):
   flag=True
   chessboard[c.translate_position(next_pos)]=chessboard[c.translate_position(curr_pos)]
   chessboard[c.translate_position(curr_pos)]='e'
   return chessboard, flag
