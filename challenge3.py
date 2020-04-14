import sys

def main():
    #nned to have a 1 arg
    if len(sys.argv) != 2:
        print 'Invalid args'
        return
        
    password = sys.argv[1]
    builder = 0
    for c in password:
        builder += ord(c)

    builder = builder << 2
    builder = ~builder
    builder = builder ^ 12648430
    builder = ~builder
    if builder == 12645638 and ord(password[0]) == 78 and len(password) == 11:
        print 'correct'
    else:
        print 'incorrect'


if __name__ == '__main__':
    main()
