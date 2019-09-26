#checkinbetween.py
def print_chessboard(chessboard):
    i=0
    for x in chessboard:
       i=i+1
       print(x+' ', end= '')
       if i%8==0:
          print('\n')
          
def checkinbetweenhorizontal(curr_pos,chessboard,next_pos): # checking horizantal a1, a2 etc
    flag=False
    if is_empty_horizontal(curr_pos,chessboard,next_pos):
         flag=True
    return chessboard,flag
  
  
def checkinbetweenvertical(curr_pos,chessboard,next_pos):    #checking vertical a1,b1,c1 etc
    flag=False
    if is_empty_vertical(curr_pos,chessboard,next_pos):
         flag=True
    return chessboard,flag   


def is_empty_horizontal(curr_pos,chessboard,next_pos):
	if curr_pos[1]<next_pos[1]:
	   y =curr_pos[0]+str(int(curr_pos[1])+1)#moving up
	   print(y)
	else: 
	   y =curr_pos[0]+str(int(curr_pos[1])-1)#moving down
	x = translate_position(y)
	if y==next_pos:
		return True
	if chessboard[x]=='e':
		return is_empty_horizontal(y,chessboard,next_pos)
	elif chessboard[x]!='e':
		return False
	return True	
def is_empty_vertical(curr_pos,chessboard,next_pos):
	if curr_pos[0]<next_pos[0]:
	    y =chr(ord(curr_pos[0])+1)+curr_pos[1] #moving right next vertical tile is a1->b1 so on
	else:
		y =chr(ord(curr_pos[0])-1)+curr_pos[1] #moving left
	x = translate_position(y)#takes a position as f5 and returns the position in list
	if y==next_pos:
		return True  #we have reached the desired position
	if chessboard[x]=='e': #empty tile, we can move
		return is_empty_vertical(y,chessboard,next_pos)
	elif chessboard[x]!='e': #not empty tile we cant go further invalid move
		return False			

def checkinbetween_diagonal(curr_pos,chessboard,next_pos):
    if curr_pos[0]<next_pos[0]:
        y =chr(ord(curr_pos[0])+1)+curr_pos[1] #moving up
    else:
        y =chr(ord(curr_pos[0])-1)+curr_pos[1]#moving down
    if curr_pos[1]<next_pos[1]:
        y =y[0]+str(int(curr_pos[1])+1)#moving to the right
    else:
        y =y[0]+str(int(curr_pos[1])-1)#moving to the left
    t = translate_position(y)#takes a position as f5 and returns the position in list
    if  y==next_pos:
        return chessboard, True  #we have reached the desired position
    if chessboard[t]=='e': #empty tile, we can move
        return checkinbetween_diagonal(y,chessboard,next_pos)
    elif chessboard[t]!='e': #not empty tile we cant go further invalid move
        return chessboard, False
    return chessboard, True
		
def translate_position(position):
    res=0
    if position[0]=='a':
      res=0   
    if position[0]=='b':
      res=1
    if position[0]=='c':
      res=2 
    if position[0]=='d':
      res=3   
    if position[0]=='e':
      res=4
    if position[0]=='f':
      res=5 
    if position[0]=='g':
      res=6
    if position[0]=='h':
      res=7
    res=res+(int(position[1])-1)*8
    return res         
