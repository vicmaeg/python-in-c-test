import math

def sum (a, b):
    return a+b

if __name__ == "__main__":
    import sys
    value = sum(int(sys.argv[1]), int(sys.argv[2]))
    print (value)