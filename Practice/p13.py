# Write a python program to find a longest word from file given by the user. 

fp = open("p1_demoOk.txt","w")

# words = fp.read().split()

# longestWord = ""

# for word in words:

#     if(len(longestWord) < len(word)):
#         longestWord = word

# print("Longest Word : " + longestWord)

fp.writelines(["hey\n","ok"])

fp.close()