

# ----------------------TCS Question 2022,------------------------|
# Mack a Game
# two player can play the this game
# Not the condition
# |---------------------------------------------------------------|
# | hear given 2D arr are "0" and "1" Value                       |
# | x--------->                                                   |
# | y  1 0 0 1                                                    |
# | |  1 1 0 0                                                    |
# | |  0 0 1 1                                                    |
# | \/ 0 1 1 0                                                    |
# |player 1 play first ---- > give a (x,y)                        |
# |(x,y) value is "0" palyer 1 play continue and                  |
# |when (x,y) value is "1" then change the value "1" to "0" and   |
# |move the player 2,                                             |
# | when arr all zero  then game is End.                          |
# |palayear point are print                                       |
# |_______________________________________________________________|


              #input 2d arr ============ user input
# x,y = int(input("Enter the x = ")),int(input('Enter the y = '))
# tdarr=[]
# for i in range(x):
#     arr= []
#     for j in range(y):
#         # print("Enter the valu ("+i+","+j+") =")
#         # print("enter the valu "+str(i)+str(j))
#         arr.append(int(input("Enter the valu ("+str(i)+","+str(j)+") =")))
#     tdarr.append(arr)

tdarr = [[1,0,0,1],[1,1,0,0],[0,0,1,1],[0,1,1,0]]
print (tdarr)
x=4
y=4
player1 = 1
point1 = 0
point2 = 0
player2 = 0
start = 1
while(start):
    k=1
    for i in range(x):
        for j in range(y):
            if( tdarr[i][j] == 1):
                k=0
    if(k == 1):
        start = 0
    else:
        print("Game is Runing")
        if(player1 == 1):
            print("play player1 = ")
            a,b=int(input("enter x value ")),int(input("enter y value "))
            if(tdarr[a][b] == 1):
                print(tdarr[a][b])
                tdarr[a][b] = 0
                point1 = point1 +1
                player1 = 0
                player2 = 1
            else:
                point1 = point1 + 1
        else:
            print("play player2 = ")
            a,b=int(input("enter x value ")),int(input("enter y value "))
            if(tdarr[a][b] == 1):
                print(tdarr[a][b])
                tdarr[a][b] = 0
                point2 = point2 +1
                player2 = 0
                player1 = 1
            else:
                point2 = point2 + 1

print("------------Game is End --------")
print("playear 1 point ")
print(point1)
print("playear 2 point ")
print(point2)
if (point1 == point2):
    print("Draw The Game")
if(point1>point2):
    print("Player 1 is Win")
else:
    print("player 2 is Win")