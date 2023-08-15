def split_and_join(line):
    line2= line.split(" ")
    line3= "-".join(line2)
    return line3
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)