def removeChar(s, c):
    
    counts = s.count(c)

    
    s = list(s)

    
    while counts:
       
        s.remove(c)

        
        counts -= 1

    
    s = ''.join(s)

    print(s)



if __name__== '_main_':
    s = "hello world"
    removeChar(s, 'l')
