# import sys
# class Queue:
#     def __init__(self, size):
#         self.myQueue = []
#         self.queueSize = size
#     def isFull(self):
#         if len(self.myQueue) == self.queueSize:
#             return True
#         else:
#             return False
        
#     def enqueue(self, value):
#         if not self.isFull():
#             self.myQueue.append(value)
#             print("Element enqueued: ", value)
#         else:
#             print("Queue is full. Cannot enqueue.")    
        
# size = int(input("Enter the size of the queue: "))
# queue = Queue(size)
# print("Queue created with size: ", queue.queueSize)
# while True:
#     print("1. Enqueue")
#     print("2. Dequeue")
#     print("3. Display")
#     print ("4. Delete Queue ")
#     print("5. peek")
#     print("6. Exit")
#     choice = int(input("Enter your choice: "))
#     if choice == 1:
#         if len(queue.myQueue) < queue.queueSize:
#             element = int(input("Enter the element to enqueue: "))
#             queue.myQueue.append(element)
#             print("Element enqueued: ", element)
#         else:
#             print("Queue is full. Cannot enqueue.")
#     elif choice == 2:
#         if len(queue.myQueue) > 0:
#             element = queue.myQueue.pop(0)
#             print("Element dequeued: ", element)
#         else:
#             print("Queue is empty. Cannot dequeue.")
#     elif choice == 3:
#         print("Current Queue: ", queue.myQueue)
#     elif choice == 4:
#         queue.myQueue.clear()
#         print("Queue deleted.")
#     elif choice == 5:
#         if len(queue.myQueue) > 0:
#             print("Front element: ", queue.myQueue[0])
#         else:
#             print("Queue is empty.")
#     elif choice == 6:
#         print("Exiting...")
#         sys.exit()
#     else:
#         print("Invalid choice. Please try again.")



# fruit = {}
# def addone(index):
#         if index in fruit:
#             fruit[index] += 1
#         else:
#             fruit[index] = 1
# addone("apple")
# addone("banana")
# addone("apple")
# print(len(fruit))


#write a program to accept student name and marks from the keyboard and create a dictionary. Also display student marks by taking student name.
# students = {}
# def add_student(name, marks):
#     students[name] = marks
# name = input("Enter student name: ")
# marks = int(input("Enter student marks: "))
# add_student(name, marks)

# name = input("Enter student name to get marks: ")
# if name in students:
#     print("Marks of ", name, " are: ", students[name])
# else:
#     print("Student not found.")

#write a program to access each character of the string in forward and backward direction by using for loop and while loop.
# Access each character of a string in forward and backward direction using while loop

# s = input("Enter a string: ")

# print("Forward direction:")
# i = 0
# while i < len(s):
#     print(s[i])
#     i += 1

# print("Backward direction:")
# i = len(s) - 1
# while i >= 0:
#     print(s[i])
#     i -= 1

# Find the missing character from sent string

# stringSent, stringRec = input().split()

# for ch in stringSent:
#     if stringSent.count(ch) != stringRec.count(ch):
#         print(ch)
#         break

# v=['a','e','i','o','u' ]
# w=input("Enter a string: ")
# found=[]
# for i in w:
#     if i in v and i not in found:
#         found.append(i)
# print("Vowels found:", found)
# print('Unique vowels count:', len(found),'from the string=',w)


# # Read input
# num, start, end = map(int, input().split())

# # Read distances
# distances = list(map(int, input().split()))

# # Find employees within range
# result = []

# for d in distances:
#     if start <= d <= end:
#         result.append(d)

# # Output
# for i in result:
#     print(i, end=" ")


# import datetime 
# # Get current date and time
# date= datetime.datetime.now()
# print("Current date and time: ", date)

# X=['A','B','C']
# Y=['A','B','C']
# z=[1,2,3,4]
# print(X==Y)
# print(X==z)
# print(X != z)

# s = [1,4,9,16,25,36,49,64,81,100]
# val=[2**i for i in range(1,6)]
# print(val)

# square={x:x*x for x in range(1,6)}
# print(square)

# a,b= [int(x) for x in input("Enter two numbers: ").split()]
# print("product: ", a*b)

# a,b,c= [float(x) for x in input("Enter three numbers: ").split(',')]
# print("The sum of the three numbers is: ", a+b+c)

# mycart=[10,20,800,60,70]
# for item in mycart:
#     if item > 400:
#         print("Expensive item: ", item)
#         continue
#     print("Affordable item: ", item)




# while True:
#     username = input("Enter username: ")
#     password = input("Enter password: ")
#     if username == 'admin' and password == 'admin':
#         print("Login successful")
#         break
#     else:
#         print("Login failed. Please try again.")


#tower of hanoi
def tower_of_hanoi(n, source, helper, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    tower_of_hanoi(n - 1, source, destination, helper)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n - 1, helper, source, destination)


# Main code
n = int(input("Enter number of disks: "))

tower_of_hanoi(n, "A", "B", "C")
