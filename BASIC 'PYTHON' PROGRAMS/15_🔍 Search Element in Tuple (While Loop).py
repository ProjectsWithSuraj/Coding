#Elements=(1,4,9,16,25,36,49,64,81,100)

list=(1,4,9,16,25,36,49,64,81,100)
x=49 #Let x be the variable for searching no.
idx=0
while idx < len(list):
    if(list[idx]==x):
        print("Number is in: ",idx)
    idx+=1