#this program keeps track of the number of arguments remaining with each iteration (simpler, isolated version)
arg_a = 1
arg_b = 2
arg_c = 3
arg_d = 4
arg_e = 5
arg_f = 6

def remaining_args(*args):
    global count
    count = len(args) #total arguments remaining
    for arg in args:
        print(f"Argument: {arg}")
        count -= 1
        print(f"Arguments Remaining: {count}")


remaining_args(arg_a, arg_b, arg_c, arg_d, arg_e, arg_f)

#another thing right here:

def remain_args(*args):
    for arg in args[:9]:
        print(arg)

remain_args(arg_a, arg_b, arg_c, arg_d, arg_e, arg_f)