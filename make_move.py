#make_move.py

import checkinbetween as c
import tower as t
import bishop as b
import pawn as p
import queen as q
import king as k
import knight as h

def make_move(curr_pos,chessboard,next_pos):
	x = chessboard[c.translate_position(curr_pos)]
	if x=='e':return chessboard,False
	elif x=='t'or x=='T':
		return t.move_tower(curr_pos,chessboard,next_pos)
	elif x=='h'or x=='H':
		return h.move_knight(curr_pos,chessboard,next_pos)
	elif x=='b'or x=='B':
		return b.move_bishop(curr_pos,chessboard,next_pos)
	elif x=='p' or x=='P':
		return p.move_pawn(curr_pos,chessboard,next_pos)
	elif x=='q' or x=='Q':
		return q.move_queen(curr_pos,chessboard,next_pos)
	elif x=='k' or x=='K':
		return k.move_king(curr_pos,chessboard,next_pos)
		
