import random
#Create the players function
def get_board(csv_file):
  op=open(csv_file)
  lis=[]
  row=op.readline().strip().split(',')
  for i in op:
    line=i.strip().split(',')
    dic={}#single tile
    for j in range(len(line)):
      dic[row[j]]=line[j]
    lis.append(dic) 
  op.close()
  return lis

#Create the players function
def get_players(n):
  lis=[]
  for i in range(0,n) :
    # name=input("please type the player's name:")#will return 'player1' if the user does not input
    # if name=='':
    dic={}
    dic['name']='Player'+str(i+1)
    dic['position']=0#start from "Go"
    dic['wallet']=1500#default
    dic['properties']=[]
    lis.append(dic)
  return lis
#the sample info would be [{name: Player 1, location: 0, cash: 1500},...]
    
#Print the game board function
def print_board(board, players):
  for i in range(len(board)):#print all the tiles
    residence=[]
    print(board[i]['name'])
    for j in range(len(players)):
      if i==players[j]['position']:#if the player is on the nst tile
        residence.append(players[j]['name'])
    if board[i]['owner']!='bank' and board[i]['owner']!='':
      print(' Owner: '+board[i]['owner'])
    if residence !=[]:
      print(' Residents: '+', '.join(residence))
      
#Print a single player function
def print_player(player, board):
  print(player['name'])
  print(' Wallet: '+str(player['wallet']))
  print(' Position: '+board[player['position']]['name'])
  print(' Properties: ')
  for i in player['properties']:
    print('   '+i)

#Property type counter function
def type_counter(player, board, tile_type):
  counter=0
  for j in board:
    if j['owner']==player and j['type']==tile_type:
      counter+=1
  print(counter)
  return counter  
  
#rent for utility
def rent_for_utility(quan,dice_roll):
  if quan==1:
    return 400*dice_roll
  elif quan==2:
    return 10*dice_roll
  
  
#Move a player around the board function
def move_player(player,board,dice_roll):
  total_tiles=len(board)
  global move
  move=random.randint(1,dice_roll)
  player['wallet']-=int(board[0]['rent'])*((player['position']+move)//total_tiles)#time of passing 'Go' 
  player['position']=(player['position']+move)%total_tiles
  print('Welcome to '+board[player['position']]['name']+'!')#arrived position
  
  
def check(player,players,board,dice_roll):
  #check the tile
  type=board[player['position']]['type']
  if type=='0':#the tile is not purchasable but funtional (the type is 0)
    print('More function of this tile is to be developed')
    
  elif board[player['position']]['owner']=='bank':#the tile is purchasable (the owner is bank and the type is not 0)
    if player['wallet']>=int(board[player['position']]['cost']):#player has enough money
      while True:
        decision=input('Would you like to buy? [y/n]:')
        if decision =='y':
          player['wallet']-=int(board[player['position']]['cost'])#spend money
          player['properties'].append(board[player['position']]['name'])#mark down the player owns the nst tile
          board[player['position']]['owner']=player['name']#mark down the owner of nst tile is the player
          break
        elif decision=='n':
          break
        
  elif board[player['position']]['owner']!='bank':
    owner=board[player['position']]['owner']
    #the tile is owned by some player
    if player['name']!=owner:
      #the tile is not owned by the player on the tile
      if type=='1':#the property is a street
        rent=int(board[player['position']]['rent'])
        player['wallet']-=rent#pay the rent
        for i in players:
          if i['name']==owner:
            i['wallet']+=rent#receive the rent
      elif type=='2':#the property is a railroad
        quantity=type_counter(owner,board,type)#the number of railroad owned by the tile's owner
        rent=25*quantity
        player['wallet']-=rent#pay the rent
        for i in players:
          if i['name']==owner:
            i['wallet']+=rent#receive the rent
      elif type=='3':#the property is a utility
        quantity=type_counter(owner,board,type)#the number of railroad owned by the tile's owner
        rent=rent_for_utility(quantity,dice_roll)
        player['wallet']-=rent#pay the rent
        for i in players:
          if i['name']==owner:
            i['wallet']+=rent#receive the rent
      

def eligible_to_pay(players,board):  
  for i in players:
    if i['wallet']<=0:
      for j in board:
        if j['owner']==i['name']:
          j['owner']='bank'#return properties to bank
        

# ######Start the game and set

#Create the game board
boardlist=get_board('monopoly.csv') 
#Create the players
number=2
playerslist=get_players(number)#decides the number of players
dice_roll_max=12
turn=0
looping=True


while looping:
  #check if there is a winner
  winner=[]
  for i in playerslist:
    if i['wallet']>0:
      winner.append(i['name'])
  if len(winner)==1:#end the game when only one player has positive money
    print('Congrats! '+winner[0]+' you win the game!')
    looping=False
    break
    
  #Interaction
  play=turn%number
  while True:
    if playerslist[play]['wallet']>0:#only when the player is not broken then he/she can play the game
      action=input(playerslist[play]['name']+'[i: info, b: board, p: play, q: quit]')

      if action=='p':#Move a player around the board
        move_player(playerslist[play], boardlist,dice_roll_max)#dice_roll determines the largest value
        check(playerslist[play],playerslist,boardlist,move)#check the payment of rent,purchasing of the tile, or whether the player is broke
        eligible_to_pay(playerslist,boardlist)
        #check whether they are eligible to pay to continue the game, or their properties would be returned to bank
        break
      elif action=='i':#Print a single player
        print_player(playerslist[play], boardlist)
      elif action=='b':#Print the game board
        print_board(boardlist, playerslist)
      elif action=='q':#Quit the loop
        looping=False
        break
    else:
       print(playerslist[play]['name']+' is broke!')
       break
  turn+=1

