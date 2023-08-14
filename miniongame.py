def minion_game(string):
    Stuart=0
    Kevin=0
    vowels=['A','E','I','O','U']
    for i in range(len(string)):
        if string[i] not in vowels:
                Stuart+=(len(string)-i)
        else:
                Kevin+=(len(string)-i)
                            
    if Stuart>Kevin:
        print('Stuart',Stuart)
    elif Stuart<Kevin:
        print("Kevin",Kevin)
    else:
        print("Draw")
                
    

