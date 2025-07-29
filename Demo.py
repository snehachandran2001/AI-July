# a=["sneha",1,2,67,("hello",3.4),[1,2,3,[12,89]],{"name":"anu"},10.5,True]
# print last element
# print 3.4
# print 12

# print(a[-1])
# print(a[4][1])
# print(a[5][3][0])
# # print anu
# print(a[6]["name"])

# adding elements
# a.append("new_element") 
# print(a)
# inserted_element = a.insert(2, "inserted_element")
# print(a)
b=[1,2,3,33,4,5]
c=[6,7,8,9]
# extend list
# b.extend(c)
# print(b)
# print(c)
# c.extend(b)
# print(c)
# change element
# b[0] = 100
# print(b)

# remove element using pop
# a=[1,2,3,4,5,6,7,8,9,4,10]
# print(a.pop(2))  # removes and returns the last element
# a.pop(2)
# print(a)
# a.pop()
# # removes and returns the last element
# print(a)

# # remove element using remove
# a.remove(4)  # removes the first occurrence of the value
# # remove all elements
# a.clear()  # clears the list
# print(a)
# # delete the list
# del a  # deletes the list variable
# print(a)  # This will raise an error since 'a' is deleted

# reverse the list

# d=[6, 7, 8, 9]
# # b.reverse()
# # print("reverse of the list",b)  # Output: [5, 4, 3, 2,
# c=b*2
# print(c)

# # length of the list
# print(len(b))  # Output: 5
# e=b+d
# print(e)  # Output: [1, 2, 3, 4,
# membership operators
# b = (1,2,3,4,5,(2,4,5,),"hello",[1, 2, (2,"python",5,),13,14,15],{"name": "anu"},10.5,True)
# print(len(b))
# print(type(b))
# access 13,14,15

# access python 
# access anu


# c= [6, 7, 8, 9,1,2,3,4,5]
# # list intersection
# d = list(set(b) & set(c))
# print(d)  # Output: [1, 2, 3, 4, 5]
# # list union
# e = list(set(b) | set(c))
# print(e)  # Output: [1, 2, 3, 4,

# print(1 in b)  # Output: True
# print(max(b))
# print(min(b))
# print(sum(b))
# count = b.count(1)  # Count occurrences of 1
# print(count)  # Output: 1



# a=int(input("enter the 1st number" ))
# b=int(input("enter the 2nd number" ))
# c=int(input("enter the 3rd number" ))
# if (a>b):
#     if(a>c):
#         print(a,"largest")
#     else:
#         print(c,"largest")
# else:
#      if(b>c):
#          print(b,"largest")
#      else:
#          print(c,"largest")

# a=int(input("Enter a number: "))
# if a>0:
#     print("Positive")
#     if a==0:
#         print("Zero")
# else:
#     if a<0:
#         print("Negative")
#     else:
#         print("Zero")
# a= int(input("Enter a number: "))
# if a==0:
#     print("Its zero")
# elif a>0:
#     print(a, "is positive")
# else:
#     print(a, "is negative")

# a=int(input("enter a number:"))
# b=int(input("enter second number"))
# c=a+b
# # print("sum=",c)
# print(f"sum of {a} and {b} is {c}")


# num=int(input("Enter the limit:"))
# i=1
# while i<=num:
#     print("*"*i)
#     i+=1

# a=int(input("Enter a number:"))
# for i in range(1,a+1):
#     print(' *'*i)

# n=int(input("Enter range: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
# def mathu():
#     a=int(input("Enter a number: "))
#     b=int(input("Enter one more number: "))
#     c=int(input("Select an operation \n 1.Addition\n 2.Substraction\n 3. Multiplication\n 4.Division\n "))
#     if c==1:
#         print(f"{a} + {b} = {a+b}")
#     elif c==2:
#         print(f"{a} - {b} = {a-b}")
#     elif c==3:
#         print(f"{a} x {b} = {a*b}")
#     elif c==4:
#         print(f"{a} / {b} = {a/b}")
#     else:
#         print("You should have written 1, 2, 3, or 4 :(")
#     return

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Select an operation: \n 1. Addition\n 2. Subtraction\n 3. Multiplication\n 4. Division\n\n"))
def sum(a, b):
    return a + b
def subi(a, b):
    return a - b
def mult(a, b):
    return a * b
def div(a, b):
    if b==0:
        return ("Nadakkoola")
    else:
        return a / b
if c==1:
    print(sum(a,b))
elif c==2:
    print(subi(a,b))
elif c==3:
    print(mult(a,b))
elif c==4:
    print(div(a,b))
else: 
    print("exit")



