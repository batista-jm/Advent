file = "db3.txt"
total = 0
enabled = True
with open(file, 'r') as file:
    read = file.read()
    txt = list(read)
    
    for x in range(len(txt) - 7):
        if txt[x] == "d" and txt[x+1] == "o" and txt[x+2] == "(" and txt[x+3] == ")":
            enabled = True
        elif txt[x] == "d" and txt[x+1] == "o" and txt[x+2] == "n" and txt[x+3] == "'"  and txt[x+4] == "t" and txt[x+5] == "(" and txt[x+6] == ")":
            enabled = False
        if enabled == True:
            if txt[x] == "m":
                if txt[x+1] == "u" and txt[x+2] == "l" and txt[x+3] == "(":
                    num1 = ""
                    num2 = ""
                
                    i = x + 4
                    while txt[i].isdigit():
                        num1 += txt[i]
                        i += 1
                    
    
                    if txt[i] == ",":
                        i += 1  
                    
                        while txt[i].isdigit():
                            num2 += txt[i]
                            i += 1
                    
                    
                        if txt[i] == ")":
                            print("cold") 
                            total += int(num1) * int(num2)

print(total)
