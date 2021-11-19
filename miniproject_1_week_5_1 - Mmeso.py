# SOB 100: PRINTING A PATTERN TO SIMULATE A BALL BOUNCING
# OFF OF A WALL USING NESTED FOR-LOOPS.

###########################################


for x in range(1,5):
    for y in range(x):
        print("*", end=" ")

    print()

for x in range(5,0, -1):
    for y in range(x):
        print("*", end=" ")

    print()








# SOB 101: PRINTING A PATTERN TO SIMULATE A BALL BOUNCING
# OFF OF A WALL USING 2D ARRAYS INSTEAD OF NESTED FOR-LOOPS.

###########################################



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




# SOB 101: PRINTING A PATTERN TO SIMULATE A BALL BOUNCING
# OFF OF A WALL USING 2D ARRAYS INSTEAD OF NESTED FOR-LOOPS.
# AS WELL AS OMITTING SOME EXTRA CHARACTERS SUCH THAT A SINGLE ASTERISK
# IS SHOWN FOR EVERY LINE, MAKING IT LOOK LIKE A BALL (THE ASTERISK) BOUNCING OFF OF A SURFACE.

###########################################



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











# SOB 101: PRINTING THE PATTERN 4 TIMES TO FORM A
# ZIG-ZAG PATTERN.

###########################################


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


for i in range(3):
    for stage in symbols:
        for x in range(len(stage)):
            if stage[x] == 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
