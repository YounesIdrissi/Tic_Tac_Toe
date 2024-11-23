#this program keeps track of the number of arguments remaining with each iteration and increments using a list
arg_a = 1
arg_b = 2
arg_c = 3
arg_d = 4
arg_e = 5
arg_f = 6
used = [] #did we make this more complicated than necessary? (maybe)

def remaining_args(*args):
    global count
    count = len(args) #the number of arguments

    while count >= 0: #when the number of arguments subceeds 0, exit the while loop
        for arg in args[len(used):len(used)+1]: #when staring out, list 'used' has a lenght of 0
            print(f"Argument: {arg}") #prints the argument within the corresponding index number
            used.append(arg)
            count -= 1 #keeps track of the number of arguments remaining
            print(f"Remaining arguments: {count}")
    print(used)

remaining_args(arg_a, arg_b, arg_c, arg_d, arg_e, arg_f)
