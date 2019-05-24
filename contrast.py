def contrast(arg1, arg2):
    if type(arg1) != str:
        return 0
    elif type(arg2) != str:
        return 0
    elif arg1 == arg2:
        return 1
    elif (len(arg1) > len(arg2)):
        return 2
    elif (arg2 == 'learn'):
        return 3
    
print(contrast(2, '2'))             # 0
print(contrast('2', 2))             # 0
print(contrast('2', '2'))           # 1
print(contrast('22', '2'))          # 2
print(contrast('222222', 'learn'))  # 2
print(contrast('22222', 'learn'))   # 3






