son = 10


match son:
    case 1:
        print("sd")
    case 2:
        print("2")

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

combined_example(1,3,kwd_only=4)

def foo(name, **kwds):
    return name in kwds

foo(1, **{"r":10})