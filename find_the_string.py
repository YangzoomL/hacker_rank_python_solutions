def count_substring(string, sub_string):
    count = 0
    len_of_sub_string= len(sub_string)
    for i in range(len(string)):
        if sub_string == string[i : len_of_sub_string]:
            count += 1
        len_of_sub_string += 1
    return count
        

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)