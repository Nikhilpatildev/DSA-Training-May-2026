name = "prashantjha" # this is our string
#012345678910


print(name[0]) #p
print(name[1]) #r
print(name[-1]) #a
#print(name[15])
print(name[0:5]) # end-1, 5-1= 4 prash
print(name[1:])  #rashantjha
print(name[:5])  # 5-1=4 prash
print(name[:]) #prashantjha
print(name[1:8:2])#'''8-1=7= rsat
print(name[::-1]) # reverse of string

s = "Python are High level programming Language"

print(s.lower())

print(s.upper())

print(s.swapcase())

print(s.title())

print(s.capitalize())

name = "prashant"
sal = 5000
age = 28

print("{} sal is {} age is{}".format(name, sal,age))
print("{0} sal is {1} age is {2}".format(name, sal, age))
print("{x} sal is {y} age is{z}".format(x=name,y=sal,z=age))
A=1

print(f"{A} is a good boy")

name = "Nikhil"
newname = ""
N = len(name)
for i in range(N-1,-1,-1):
    newname += name[i]
print(newname)

#palindrome

name = "naman"
if name == name[::-1]:  
    print("Palindrome") 
else:    print("Not Palindrome")

#count vowels and consonants
name = "Nikhil"
print(name)
vowels = 0  
consonants = 0
for i in name:
    if i in "aeiouAEIOU":
        vowels += 1
    else:
        consonants += 1
print("Vowels:", vowels)
print("Consonants:", consonants)

#Anagram
name1 = "listen"
name2 = "silent"
if sorted(name1) == sorted(name2):
    print("Anagram")
else:
    print("Not Anagram")

    #pangram
sentence = "The quick brown fox jumps over the lazy dog"
alphabet = "abcdefghijklmnopqrstuvwxyz"
for char in alphabet:
    if char not in sentence.lower():
        print("Not Pangram")
        break
else:    print("Pangram")

#count words in a string
sentence = "Hello world, welcome to Python programming!"
words = sentence.split()
print("Number of words:", len(words))

#reverse words in a string
sentence = "Hello world"
words = sentence.split()
reversed_sentence = ' '.join(reversed(words))
print(reversed_sentence)

#BODMAS
a=50
b=30
c=20
d=10
print(a+b*c/d) # 50+30*20/10= 50+60=110
print(a+(b*c)/d) # 50+(30*20)/10= 50+60=110
print(a+b*c/d) # 50+30*20/10= 50+60=110

# #TCS question

# message = input("Enter the message: ")

# count = 0

# for ch in message:
#     if not ch.isalnum():   # checks special characters and spaces
#         count += 1

# print("Number of special characters and whitespaces:", count)

#title case a sentence
sentence = "hello world, welcome to python programming!"
title_case_sentence = sentence.title()
print(title_case_sentence)

#check for subquence
def is_subsequence(s1, s2):
    it = iter(s2)
    return all(char in it for char in s1)   
s1 = "abc"
s2 = "ahbgdc"
print(is_subsequence(s1, s2))  # Output: True





print('prashantjha777'.isalnum())      # True

print('prashantjha'.isalpha())         # True

print('777f'.isdigit())                # False

print('sdsdsdsd'.islower())            # True

print(''.islower())                    # False

print('PRASHANTJ'.isupper())           # True

print('My Name Is Prashant'.istitle()) # True

print("Hello World".istitle())         # True

print('   '.isspace())                 # True

print("Hello".startswith("He"))        # True

print("Hello".endswith("lo"))          # True


print("Nikhil".find("hi"))                # 2
print("Nikhil".index("hi"))               # 2
print("Nikhil".count("N"))               # -1

#nested loop

for i in range(1, 4):
    for j in range(1, 4):
        print(i,end="")
    print()


# n=int(input("Enter the number of rows: "))
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print(chr(64 + j), end="")
#     print()

# n=int(input("Enter the number of rows: "))
# for i in range(1, n + 1):
#     for j in range(1, 1+i):
#         print("*", end=" ")
#     print()

# n=int(input("Enter the number of rows: "))
# for i in range(1, n + 1):
#     for j in range(1,n+2-i):
#         print(chr(64 + j), end=" ")
#     print()

# import time
# n=int(input("Enter the number of rows: "))
# for i in range(1, n + 1):
#     print(" "*(n-i), end=" ")
#     for j in range(1, i+1):
#         time.sleep(0.5)
#         print("*", end=" ")
#     print()

    #product of array except self
arr = [1, 2, 3, 4]

n = len(arr)

output = [1] * n

# Left products
for i in range(1, n):
    output[i] = output[i - 1] * arr[i - 1]

# Right products
right = 1

for i in range(n - 1, -1, -1):
    output[i] = output[i] * right
    right = right * arr[i]

print(output)

#moves zeros to end
arr = [0, 1, 0, 3, 12]
n = len(arr)
j = 0
for i in range(n):
    if arr[i] != 0:
        arr[j] = arr[i]
        j += 1
for i in range(j, n):
    arr[i] = 0
print(arr)
