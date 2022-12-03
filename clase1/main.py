class Error(Exception):
    pass
    num_integer = 0
    
    while(num_integer < 1):
        n = input("Type an integer number: ")
        try:
            n=int(n)
            if(n < 10):
                print("number is integer and smaller than 10")
            else:
                raise(ValueError, "number is bigger than 10")
                
        except ValueError:
            num_integer += 1 
raise(ValueError, "Wrong Value")

try:
    text = open("text.txt", "r")
    lines = text.readlines()
    print(lines)
except IOError:
    print("Text not found or cannot read it") 
finally:
    text.close() 
    print("Closed")


    


