# pyramid
row = int(input("Enter number of rows for pyramid:"))
for i in range(1 , row +1):
    print(" "*(row-i)+"*"*(2*i -1))
    
# pyramid
row = int(input("Enter number of rows for pyramid:"))
for i in range(row-1 , 0 ,-1):
    print(" "*(row-i)+"*"*(2*i -1))
    
# Right-Angled Triangle (Aligned to the Right)
row = int(input("Enter number of rows for Right-Angled Triangle(Aligned to the Right):"))
for i in range(1,row+1):
    print(" "*(row-i)+ "*"*i)
    
# Right-Angled Triangle (Aligned to the left)
row = int(input("Enter number of rows for Right-Angled Triangle(Aligned to the left):"))
for i in range(1,row+1):
    print("*"*i + " "*(row - i))

# Right-Angled triangle (Aligned towards upwards)
row = int(input("Enter number of rows for Right-Angled Triangle(Aligned towards upwards):"))
for i in range(row,0,-1):
    print("*"*i)
    
# Right-Angled triangle (Aligned towards downwards)
row = int(input("Enter number of rows for Right-Angled Triangle(Aligned towards downwards):"))
for i in range(row,0,-1):
    print(" "*(row-i)+"*"*i)
    
# Right-Angled triangle (Aligned towards downwards)
row = int(input("Enter number of rows for Right-Angled Triangle(Aligned towards downwards):"))
for i in range(row,0,-1):
    print(" "*(row-i)+"*"*i)



    
    
   
