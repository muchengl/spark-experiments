import sys
import os

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("No input argvs!")
        print("Ex: python3 cut_data_set.py 1 1Mb.txt")
        sys.exit(1)

    filesize = sys.argv[1]
    filename = sys.argv[2]

    chunk_size = 1024 * 1024 # 1Mb

    data_source = '/home/grads/l/liu.hz/data_set/wiki.en.text'
    
    with open(data_source, 'r') as data:
        for i in range(0,int(filesize)):
            
            content = data.read(chunk_size)

            with open(filename, 'a') as file:
                file.write(content)

print("Finish")