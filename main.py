#TEST Code. 
 
import secrets 

current_player = secrets.choice(players)

play = True
players = [1,2]
while play:
	game = [[0, 0, 0],
        	[0, 0, 0],
        	[0, 0, 0]]





def(current_game):
	for row in game:
		print(row)
		if row.count(row[0])==len(row) and row[0] !=0:
			print(f"Player {row[0]} has won horizontally!")

	for col in range(len(game[0])):
		check[]
		for row in game:
			check.append(row[col])
		if check.count(check[0]) == len(check) and check[0] !=0:
			print(f"The player {row[0]} has von vertically! ")


	diag = []
	for i in range(len(game)):
		diag.append(game[i][i])

	if diag.count(diag[0]) == len(diag) and diag !=0:
		print(f"Player {diag[0]} has won diagonnaly ")

	for i, rev_i in enumerate(reversed(range(len(game)))):
		diag.append(game[i][rev_i]) 
		
	if diag.append(diag[0])==len(diag) and diag!=0:
		print(f"Player {diag[0]} has won diagonnaly /")


def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        print("   0  1  2")
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map
    except IndexError:
        print("Did you attempt to play a row or column outside the range of 0,1 or 2? (IndexError)")
        return False
    except Exception as e:
        print(str(e))
        return False


game = game_board(game_board, player=1, row=1, column=1)




#Check mutability

game1 = [[0,0,0],[0,0,0],[0,0,0]]
print(game1)
print(id(game1))

def game_b():
	global game1
	print(game1)
	game1 = [[0,0,0],[0,0,1],[0,0,0]]
	print(game1)	
	print(id(game1))

	return game1

game_b()
print (game1)
print(id(game1))


#When you win horizontally

game = [[1, 0, 0],
        [2, 2, 0],
        [2, 1, 2]]

def win(current_game):
	for row in game:
		print (row)
		column1= row[0];
		column2=row[1]
		column3=row[2]

		if column1 == column2 == column3 and column1 != 0:
			print("WIN")

win(game)

#Horizontal Rows Matching

game = [[1, 0, 1],
        [2, 0, 2],
        [2, 2, 2]]

def win(current_game):
	for row in game:
		print (row)
		if row.count(row[0]) == len(row) and row[0] !=0:
			print(f"The winner is {row[0]} ")
			print(row[0])


win(game)

#Vertical Rows Matching
game = [[1,0,1], 
		[1,1,2],
		[1,2,2]]

check = []
print(type(check))

for row in game:
	print(row)
	check.append(row[0])

if check.count(check[0]) == len(check):
	print("Winner")
	print(len(game))

