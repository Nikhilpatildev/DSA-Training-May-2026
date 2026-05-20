# class Tree:
#     def_init__(self, data)
#     self.data = data
#     self.child = []

# rootNode = Tree("Drinks")
# hot = Tree("Hot")
# cold = Tree("Cold")
# tea = Tree("Tea")
# coffee = Tree("Coffee")
# NonAlcoholic = Tree("Non-Alcoholic")
# Alcoholic = Tree("Alcoholic")

# rootNode.child.append(hot)
# rootNode.child.append(cold)


class Tree:
    def __init__(self, data):
        self.data = data
        self.child = []

    def __str__(self, level=0):
        ret = "\t" * level + repr(self.data) + "\n"
        for child in self.child:
            ret += child.__str__(level + 1)
        return ret

    def addChild(self, object):  
        self.child.append(object) 
        print("Tree node added successfully")

rootNode = Tree("Drinks")
hot = Tree("Hot")
cold = Tree("Cold")
Tea = Tree("Tea")
Coffee = Tree("Coffee")
NonAlcoholic = Tree("Non-Alcoholic")
Alcoholic = Tree("Alcoholic")

rootNode.addChild(hot)
rootNode.addChild(cold)
hot.addChild(Tea)
hot.addChild(Coffee)
cold.addChild(NonAlcoholic)
cold.addChild(Alcoholic)

print(rootNode)

# Tree Node Example in Python

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Creating Nodes
N1 = Node("N1")
N2 = Node("N2")
N3 = Node("N3")
N4 = Node("N4")
N5 = Node("N5")
N6 = Node("N6")
N7 = Node("N7")
N8 = Node("N8")

# Connecting Nodes
N1.left = N2
N1.right = N3

N2.left = N4
N2.right = N5

N3.right = N6

N4.left = N7
N4.right = N8


# Function to print tree (Preorder Traversal)
def preorder(node):
    if node:
        print(node.value, end=" ")
        preorder(node.left)
        preorder(node.right)

print("Preorder Traversal of Tree:")
preorder(N1) 


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Step 1: A new node initially points to None

class LinkedList:
    def __init__(self):
        self.head = None  # The list starts empty

    def insert_at_tail(self, data):
        new_node = Node(data)

        # Step 2: Handle the empty list edge case
        if self.head is None:
            self.head = new_node
            return

        # Step 3: Traverse starting from the head to find the last node
        current = self.head
        while current.next is not None:
            current = current.next

        # Step 4: Link the old tail's next pointer to our new node
        current.next = new_node

    def display(self):
        """Helper method to print the list elements sequentially."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> None")

# --- Example Usage ---
if __name__ == "__main__":
    llist = LinkedList()
    
    llist.insert_at_tail(10)
    llist.insert_at_tail(20)
    llist.insert_at_tail(30)
    
    # Visual Output: 10 -> 20 -> 30 -> None
    llist.display()

#array rotation
def rotate_array(arr, k):
    n = len(arr)
    k = k % n  # Handle cases where k > n
    return arr[-k:] + arr[:-k]
# Example usage
arr = [1, 2, 3, 4, 5]
k = 2
rotated_arr = rotate_array(arr, k)
print(rotated_arr)  # Output: [4, 5, 1, 2, 3]

# largest subarray with sum zero
def largest_zero_sum_subarray(arr):
    sum_index_map = {}
    max_length = 0
    current_sum = 0

    for i in range(len(arr)):
        current_sum += arr[i]

        if current_sum == 0:
            max_length = i + 1
        elif current_sum in sum_index_map:
            max_length = max(max_length, i - sum_index_map[current_sum])
        else:
            sum_index_map[current_sum] = i

    return max_length
# Example usage
arr = [1, -1, 3, 2, -2, 5, -3]
result = largest_zero_sum_subarray(arr)
print(result)  # Output: 5 (subarray [3, 2, -2, 5, -3])

#remove leading zeros from a list of integers
def remove_leading_zeros(arr):
    while arr and arr[0] == 0:
        arr.pop(0)
    return arr
# Example usage
arr = [0, 0, 1, 2, 3]
result = remove_leading_zeros(arr)
print(result)  # Output: [1, 2, 3]