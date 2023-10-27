

cases = int(input()) 

for i in range(cases): #go through the other lines
    line = input()
    
    line = line.split(" ") #split up the line by spaces
    line[0] = int(line[0])
    if line[1] == "true" or line[1] == "True":
        line[0] -= 5
  

    if line[0] <= 60:
        print("no ticket")
        
    if line[0] >=61 and line[0] <=80:
        print("small ticket")

    if line[0] >= 81:
        print("big ticket")

   
   
        


