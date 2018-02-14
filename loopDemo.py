#Shaylee McBride
#14Feb2018
#loopDemo.py - how to use for and while loops

"""
#I love cs 5 times
for i in range(0,5): #variable does not need to be i, doesn't do last number
    print('I <3 computer science!')
""""""
i = 0
while i<5:
    print('I <3 computer science!')
    i = i+1 #update step
"""

"""
#Count from 1 to 10
for i in range(1,11):
    print(i)
""""""
i = 0
while i<10:
    i += 1 #means add 1 to i
    print(i)
"""    
    
"""
#Count from 27 to 43 by 2s
for i in range(27,44,2): #can add third number for step
    print(i)
""""""   
i = 27
while i<=43:
    print(i)
    i += 2
"""

"""
#add up the numbers from 1 to 5
total = 0
for i in range(1,6):
    total = total + i
print(total)
"""
total = 0
i = 1
while i<=5:
    total = total + i
    i += 1
print(total)



