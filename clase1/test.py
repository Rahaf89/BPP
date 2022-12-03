try:
    text = open("text.txt", "r")
    lines = text.readlines()
    print(lines)
except IOError:
    print("Text not found or cannot read it") 
finally:
    print("I read the file without problems, finished and close")
    text.close() 
    