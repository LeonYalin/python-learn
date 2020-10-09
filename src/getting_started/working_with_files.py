from ..util import print_cmd


def working_with_files():
    print_cmd('Working with files', """

    Reading and writing files:
    open(filename, mode, encoding)
    mode = read/write/append, text/binary => rt, wb ect...
    """)

    try: 
        f = open('./words.txt', mode='rt', encoding='UTF-8')
        for line in f:
            print(line)
        # f.readline() # read one line from file
        # f.readlines() # get list of lines
        # f.read(32) # read first 32 bytes of the file
        # f.seek(0) # mode the pointer to the start of the file. Can receive only 0 or the result of f.tell() command
        # f.write('lalala') # only in write mode
        # f.writelines(['lalala\n', 'second line lalala\n']) # only in write mode
    finally:
        f.close()

    # or (better) use context managers
    with open('./words.txt', mode='rt', encoding='UTF-8') as f:
        print([f'{len(line.split())} word/s in line' for line in f.readlines()])


def working_with_files_main():
    working_with_files()
