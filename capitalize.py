def solve(s):
    names = s.split(' ')
    word_list = [ ]
    for i in names :
        capitalize = i.capitalize()
        word_list.append(capitalize)
    
    final = " ".join(word_list)
    
    return(final)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()