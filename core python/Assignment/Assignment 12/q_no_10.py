# Python Program to Take in Two Strings and Display the Larger String
# without Using Built-in Functions

s1="python"
s2="programming"

count1=0
count2=0

for ind in range(0,len(s1)):
    count1=count1+1

for ind in range(0,len(s2)):
    count2=count2+1

if(count1>count2):
    print("Larger string=".s1)

else:
    print("Larger string=",s2)