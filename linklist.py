# class New:
#     def __init__(self):
#         self.a = 10

# Obj1 = New()
# Obj2 = New()
# Obj3 = New()
# Obj1.a = 20
# print(Obj1.a)
# print(Obj2.a)
# print(Obj3.a)

# Class New:
# a = 10

# def __init__(self):
#     self.name = "Python"
# Obj1 = New()
# Obj2 = New()
# Obj3 = New()
# New.a=50
# print(Obj1.a)



# class College:
   # Class variable (Static variable) - shared by all instances
#     collegename = "Modern College" 

#     def __init__(self):
#         # Instance variable - unique to each instance
#         self.studentname = "prashant" 

# # Object creation (3 separate objects)
# principal = College() 
# teacher = College()
# accountant = College()

# print("--- Initial State ---")
# print("principal  =", principal.collegename, "....", principal.studentname)
# print("teacher    =", teacher.collegename, "....", teacher.studentname)
# print("accountant =", accountant.collegename, "....", accountant.studentname)

# print("\n--- After Modifications ---")
# # Modifying the static/class variable using the Class name
# College.collegename = "HBD" 

# # Modifying the instance variable for the 'principal' object only
# principal.studentname = "prashant jha"

# print("principal  =", principal.collegename, "|", principal.studentname)
# print("teacher    =", teacher.collegename, "|", teacher.studentname)
# print("accountant =", accountant.collegename, "|", accountant.studentname)



# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

# LinkedList = LinkedList()
# LinkedList.head = Node(5)
# second = Node(10)
# third = Node(15) 
# fourth = Node(20)  

# #connecting nodes
# LinkedList.head.next = second
# second.next = third
# third.next = fourth
# # Traversing the linked list
# current = LinkedList.head
# while current is not None:
#     print(current.data)
#     current = current.next

# class Node:
#     def __init__(self, data):
#         self.data = data #instance variable
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None

# if __name__ == '__main__':
#     object = LinkedList()
#     while True:
#         print('1. Add Node LinkedList : ')
#         print('2. Add Node in Begginning : ')
#         print('3. Add Node in Between : ')
#         print('4. Add Node in End : ')
#         print('5. Display Linked List : ')
#         print('6. Exit : ')
#         ch = int(input('Enter your choice:'))
#         if ch ==1:
#             value = int(input('Enter value for node: '))
#             object.addNode(value)
#             print('None added successfully in single Linkedlist: ')


# Find the first non-repeating character in a string

# s = input("Enter a string: ")

# for ch in s:
#     if s.count(ch) == 1:
#         print("First non-repeating character:", ch)
#         break
# else:
#     print("No non-repeating character found")

# # Generate Pascal's Triangle

# n = int(input("Enter number of rows: "))

# triangle = []

# for i in range(n):
#     row = [1] * (i + 1)

#     for j in range(1, i):
#         row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

#     triangle.append(row)

# for row in triangle:
#     print(row)

    # Linked List: Add nodes and print nodes

class Node:
    def __init__(self, data):
        self.data = data      # stores value
        self.next = None      # stores address of next node


class LinkedList:
    def __init__(self):
        self.head = None      # initially linked list is empty

    def add_node(self, data):
        new_node = Node(data)     # create new node

        if self.head is None:
            self.head = new_node  # first node becomes head
        else:
            temp = self.head

            while temp.next is not None:
                temp = temp.next  # move to last node

            temp.next = new_node  # connect last node to new node

    def print_list(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Main code
ll = LinkedList()

ll.add_node(10)
ll.add_node(20)
ll.add_node(30)
ll.add_node(40)

ll.print_list()
