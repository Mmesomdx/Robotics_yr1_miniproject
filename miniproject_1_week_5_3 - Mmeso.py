#SOB 101: IDENTICAL TO ABOVE BUT THE PATTERN IS REPEATED
# 3 TIMES TO CREATE A ZIG-ZAG PATTERN


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
