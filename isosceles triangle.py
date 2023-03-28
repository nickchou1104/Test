for triangle in range(1,4):
    for layer_1 in range(1,4-triangle):
        print(" ",end="")
    for layer_2 in range(1,triangle+1):
        print("* ",end="")
    print("")

