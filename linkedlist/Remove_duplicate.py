# Python program for the above approach
class Node:
	def __init__(self):
		self.data = 0
		self.next = None

# Function to insert a node at
# the beginning of the linked list


def push(head_ref, new_data):

	# allocate node
	new_node = Node()

	# put in the data
	new_node.data = new_data

	# link the old list of the new node
	new_node.next = (head_ref)

	# move the head to point to the new node
	head_ref = new_node
	return head_ref

# Function to print nodes in a given linked list


def printList(node):
	while (node != None):
		print(node.data, end=" ")
		node = node.next


# Function to remove duplicates
def removeDuplicates(head):
	track = {}
	temp = head

	while(temp != None):
		if (not temp.data in track):
			print(temp.data, end=" ")
        
		track[temp.data] = True
        print(track)
		temp = temp.next


# Driver Code
head = None

# Created linked list will be 11->11->11->13->13->20
head = push(head, 20)
head = push(head, 13)
head = push(head, 13)
head = push(head, 11)
head = push(head, 11)
head = push(head, 11)
print("Linked list before duplicate removal ", end=" ")
printList(head)
print("\nLinked list after duplicate removal ", end=" ")
removeDuplicates(head)

# This code is contributed by _Saurabh_jaiswal
