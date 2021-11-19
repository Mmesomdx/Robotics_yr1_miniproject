#SOB 101: PRINT ASTERISK PATTERN USING A 2D LIST
# TO SIMULATE A BALL BOUNCING OFF OF A WALL.

symbols = [[0,1,0,0,0,0,0,0,0,0],
           [0,1,1,0,0,0,0,0,0,0],
           [0,1,1,1,0,0,0,0,0,0],
           [0,1,1,1,1,0,0,0,0,0],
           [0,1,1,1,1,1,0,0,0,0],
           [0,1,1,1,1,1,1,0,0,0],
           [0,1,1,1,1,1,0,0,0,0],
           [0,1,1,1,1,0,0,0,0,0],
           [0,1,1,1,0,0,0,0,0,0],
           [0,1,1,0,0,0,0,0,0,0],
           [0,1,0,0,0,0,0,0,0,0],
           ]


for stage in symbols:
    for x in range(len(stage)):
        if stage[x] == 1:
            print("*", end=" ")
    print()




#SOB 101: PRINT ASTERISK PATTERN USING A 2D LIST
# TO SIMULATE A BALL BOUNCING OFF OF A WALL AS WELL
# AS OMITTING EXTRA ASTERISK CHARACTERS SUCH THAT FOR EVERY
# ROW, ONLY ONE ASTERISK WILL BE PRINTED, TO SIMULATE A
# MOVING OBJECT, THE BALL.


symbols = [[1,0,0,0,0,0,0,0,0,0],
           [0,1,0,0,0,0,0,0,0,0],
           [0,0,1,0,0,0,0,0,0,0],
           [0,0,0,1,0,0,0,0,0,0],
           [0,0,0,0,1,0,0,0,0,0],
           [0,0,0,0,0,1,0,0,0,0],
           [0,0,0,0,1,0,0,0,0,0],
           [0,0,0,1,0,0,0,0,0,0],
           [0,0,1,0,0,0,0,0,0,0],
           [0,1,0,0,0,0,0,0,0,0],
           [1,0,0,0,0,0,0,0,0,0],
           ]


for stage in symbols:
    for x in range(len(stage)):
        if stage[x] == 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()



