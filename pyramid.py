import numpy as np 

# function to test if a number is prime or not

def is_primer(n) :
    if n <= 1 :
        return False
    for i in range(2, n) :
        if (n % i == 0) :
            return False
    return True


# Step1: fill the list with the elements of the file
C=0
with open('file.txt','r') as f: #open file
    text=f.readlines() # put the lines of the file in the variable text
    NumberOfLine = len(text) 

m = [np.inf] * NumberOfLine #initailize a list with the minus infinite value
for i in range(NumberOfLine):
    m[i]= text[i].split() #  "0 1 2 3 4 5 6 7 8 9" => ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

m = [[1], [8,4], [2, 6, 9],[0, 0, 0,3],[2, 2, 2,2,9]]
for i in range(len(m)):
    for j in range(len(m[i])):
        m[i][j]=int(m[i][j]) #convert all elements of the list to integer 
# in the example above m = [[1], [8,4], [2, 6, 9],[8, 5, 9,3]] 

f.close() #close file

# Step2: replace all prime elements with the value minus infinity
for i in range(len(m)):
    for j in range(len(m[i])):
        if is_primer(m[i][j]):
            m[i][j]=-np.Inf
            
# Step3: there are two cases to deal with: if there is a line that contains only prime numbers or not

for i in range(len(m)):
    if m[i].count(-np.Inf)==len(m[i]): # test if in a line all numbers are prime
        C=2     
        break
        #stop in this line, this line will be the maximum line that can be reached

if C==2:
    cpt=i-1 
else: #there is no line that contains only prime numbers 
    cpt=len(m)-1 # we can reach the base of the pyramid
    
#cpt is the number of the line where we will stop
 
for i in range(len(m[i])-1,0,-1): # move from the bottom to the top of the pyramid
    print("niveau "+str(i))
    if(m[i].count(-np.Inf)!=len(m[i])) :
        for j in range(0,len(m[i-1])): # go through the pyramid from right to left
            if max([m[i][j+1],m[i][j]]) != -np.Inf :
                m[i-1][j]=m[i-1][j]+max([m[i][j+1],m[i][j]]) 
            #print(m)
    
#Step 5: find the longest path       
print(m[0][0]) #the top of the pyramid is the maximum value