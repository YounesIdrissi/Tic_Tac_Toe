a = 1
b = 2
c = 3
d = 4
e = 5
f = 6
index = -1 #0 is starting index, so since there first arg has not been run, index sits before 0 (-1)
def consecutive_args(*args):
    global index
    #must find number of indexes in args and divide by number of args taken per block execution
    #take current index and subtract it from args amount to get how many args remain
    print(len(args))
    for arg in args[:2]:
        print(arg)
        index += 1
        print(f"index: {index}")


consecutive_args(a,b,c)
