# about list functions
#listt=[5,1,2,3]
# listt.append(4)
#print(listt)

#dir(listt)

#listt.sort()
#print(listt)
#listt.remove(1)
#print(listt)
#last value is gone
#listt.pop()
#print(listt)

#Lambda

def old_sum(a,b):
    return a+b

old_sum(4,5)

new_sum=lambda a,b:a+b

new_sum(7,8)

#map

saleries = [1000,2000,3000,4000]

for salery in saleries:
     print(salery*2)
     
list(map(lambda x: x*2, saleries))    
