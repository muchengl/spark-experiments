import sys
import os

def read_words_large_line(filename):
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                yield word

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("No input argvs!")
        print("Ex: python3 cut_data_set.py 1024 1kb.txt")
        sys.exit(1)

    filesize = sys.argv[1]
    filename = sys.argv[2]

    data_source = '/home/grads/l/liu.hz/data_set/wiki.en.text'
    word_generator = read_words_large_line(data_source)

    print("will wirte",filesize," into ",filename)
    for word in word_generator:
        # print(word)
        with open(filename, 'a') as file:
            file.write(word)
            file.write(" ")
        
        now_file_size = os.path.getsize(filename)
        if now_file_size>=int(filesize) :
            break

print("Finish")


