# num1 = int(input("Enter Num1 : "))
# num2 = int(input("Enter Num2 : "))

# print((num1>=num2))


# 2

# Exactly ✅ — all three methods you listed in Python do not modify the original string because strings in Python are immutable (they cannot be changed after creation).

# str = "Apple"

# print(str[1:])

# s = "hello world"

# print(s.capitalize())       # Output: "Hello world"
# print(s.replace("world", "Python"))  # Output: "hello Python"
# print(s.find("world"))      # Output: 6

# print(s)  # Original string is unchanged: "hello world"



# 3

# num1 = int(input("Enter Num1 : "))
# num2 = int(input("Enter Num2 : "))
# num3 = int(input("Enter Num3 : "))

# # max = ((num3,num2)[num2>num3],(num3,num1)[num1>num3])[num1>num2]

# if(num1>num2):
#     if(num1>num3):
#         print("max : ",num1)
#     else:
#         print("max : ",num3)

# else:
#     if(num2>num3):
#         print("max : ",num2)
#     else:
#         print("max : ",num3)
    

# 4 WAP to ask the user to enter names of their 3 favorite movies & store them in a list.

# list = []

# m1 = input("enter fav movie1 : ")
# m2 = input("enter fav movie2 : ")
# m3 = input("enter fav movie3 : ")

# list.append(m1)
# list.append(m2)
# list.append(m3)

# or

# list.append(input("enter fav movie1 : "))
# list.append(input("enter fav movie2 : "))
# list.append(input("enter fav movie3 : "))

# print(list)



# 5 WAP to check if a list contains a palindrome of elements.

# list = [1,2,3,2]
# list2 = [1,"abc","abc",1]

# # temp = list.reverse()  # aa return kai return nathi kartu so apde aa method mno kari sakiyee khass yaad rakhvu
# # temp2 = list2.reverse()

# temp = list.copy()
# temp2 = list2.copy()

# temp.reverse()
# temp2.reverse()

# if(list == temp):
#     print("yes it's palindrome")
# else:
#     print("no")


# 6 WAP to count the number of students with the "A" grade in the following tuple.
# Store the above values in a list & sort them from "A" to "D".

# stu = ("C","D","A","A","B","B","A")
# print(stu.count("A"))

# s = list(stu) # for convert tupple to list

# list.sort()

# print(list)


# # 7 Store following word meanings in a python dictionary :
# table : "a piece of furniture", "list of facts & figures"
# cat : "a small animal"

# dict = {
#     "table" : ["a piece of furniture", "list of facts & figures"],
#     "cat" : "a small animal"
# }

# print(dict["table"])


# 8 You are given a list of subjects for students. Assume one classroom is required for 1
# subject. How many classrooms are needed by all students.
# "python", "java", "C++" , "C++","C"
# "java", "python"
# "python", "javascript",
# "java"

# set = {"python", "java", "C++" , "C++","C","java", "python","python", "javascript","java"}

# print(len(set))



# 9 WAP to enter marks of 3 subjects from the user and store them In a dictionary. Start with
# an empty dictionary & add one by one. Use subject name as key & marks as value.


# dict = {}  # Start With Empty Dict

# dict.update({input("Enter Subject1 Name : ") : int(input("Enter Subject1 Mark : "))})
# dict.update({input("Enter Subject2 Name : ") : int(input("Enter Subject2 Mark : "))})
# dict.update({input("Enter Subject3 Name : ") : int(input("Enter Subject3 Mark : "))})

# print(dict)


# 10 Figure out a way to store 9 & 9.0 as separate values in the set.
# (You can take help of built-in data types)

# nums = set()

# # nums.add(9)
# # nums.add("9.0")

# # or

# nums.add(("int",9))
# nums.add(("float",9.0))


# print(nums)



# 11 Print numbers from 1 to 100.

# for i in range(101):
#     print(i)




# 12 Print numbers from 100 to 1.

# for i in range(100,0,-1):
#     print(i)




# 13 Print the multiplication table of a number n.

# n = int(input("Enter Number : "))

# for i in range(11):
#     print(n," * ",i," = ",(n*i))



# 14 WAP to find the sum of first n numbers. (using while)

# n = int(input("Enter Number : "))

# sum = 0 
# count = 1

# while count <= n:
#     sum+=count
#     count+=1

# print(sum)




# 15 WAP to find the factorial of first n numbers. (using for)

# n = int(input("Enter Number : "))

# fac = 1

# for i in range(n,0,-1):
#     fac *= i

# print(fac)




# 16 WAF to print the length of a list. ( list is the parameter)

# def list_len(list):

#     count = 0

#     for el in list:
#         count+=1
#     else:
#         return count

# print(list_len([1,2,3,4,5]))




# 17 WAF to print the elements of a list in a single line. ( list is the parameter)

# def print_list(list):

#     for el in list:
#         print(el,end=" ")


# print_list([1,2,3,4,5])




# 18 WAF to convert USD to INR.


# def convert_USD_to_INR(u):

#     print("rupees : ",88.8983 * u)

# convert_USD_to_INR(5)



# File IO

# f = open("p1_demo.txt","r")

# # data = f.read()     # Akhi File Read Kari Nakhse Pachi Cursor Last ma vi jase so Have Apde readline karisu to have empty line avse karne k file ma last line pachi kai lakhel hase nai so
# # print(data)

# line1 = f.readline()
# print(line1)
# line2 = f.readline()
# print(line2)


# f.close()


# 19 Create a new file "practice.txt" using python. Add the following data in it:
# WAF that replace all occurrences of "java" with "python" in above file.

# def replaceWord(str,str2):

#     with open("p1_demo.txt","r") as f:
        
#         data = f.read()


#     with open("p1_demo.txt","w") as f:

#         f.write(data.replace(str,str2))
        

# replaceWord("Java","Python")




# 20 Search if the word "learning" exists in the file or not.

# def searchWord(str):

#      with open("p1_demo.txt","r") as f:
        
#         data = f.read()

#         if(data.find(str) != -1):   or if(word (here str) in data)
#             print("Found",str)
        
#         else:
#             print("Not Found")

# searchWord("learning")




# 21 WAF to find in which line of the file does the word "learning"occur first.
# Print -1 if word not found.

# def whichLine(str):

#     with open("p1_demo.txt","r") as f:

#         count = 0

#         line = True

#         while line:

#             count += 1

#             line = f.readline()

#             if(str in line):
#                 print("At Line No.",count)
#                 return
        
#         if line == "":
#             print("-1")

# whichLine("learning")




# 22 Create student class that takes name & marks of 3 subjects as arguments in constructor.
# Then create a method to print the average.

# class Student :

#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks

#     def avg(self):

#         sum = 0

#         for el in self.marks:
#             sum += el

#         return sum/len(self.marks)
    
# s1 = Student("vi",[99,97,99])

# print(s1.avg())




# 23 Create Account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance.


class Acc:

    def __init__(self,balance,accNo):
        self.balance = balance 
        self.accNo = accNo

    def debit(self,amount):
        self.balance -= amount 

    def credit(self,amount):
        self.balance += amount

    def showBalance(self):     
        print(self.balance)

a1 = Acc(100000,101)

a1.showBalance()
a1.debit(1000)
a1.showBalance()
a1.credit(100000)
a1.showBalance()

