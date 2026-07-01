# dict = {}
# li = [10,10,10,20,20,30]
# for i in li:
#     if(dict.get(i,"NA") == "NA"):
#         dict.setdefault(i,li.count(i))

# print(dict)


#2 


# def total(*nums):
#     print(type(nums))  # tuple
#     return sum(nums)

# print(total(1, 2, 3, 4))



#3 


# a = 1,2,3,4

# b,*c = a 

# print(type(c))   # list



#4


# def student(**data):
#     for k, v in data.items():
#         print(k, ":", v)

# student(name="Vibhu", age=21)