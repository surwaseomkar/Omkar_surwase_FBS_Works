# Write a Python program to find the longest common prefix of all
# strings. Use the Python set.

strings={"flower","flow","flight"}

prefix=""

for i in range(len(min(strings ,key=len))):
    char={word[i] for word in strings}

    if len(char)==1:
        prefix=prefix+list(char)[0]
    else:
        break

print("Longest common prefix=",prefix)