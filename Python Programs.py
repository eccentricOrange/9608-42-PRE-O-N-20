# # 9608/42/PRE/O/N/20
# Last edited: Anuj Verma, 23:53 11/10/2020


# This is all the program code for the solution.
# The code below declares a subroutine to insert new elements, and one to traverse the linked list and print out its elements.

def insert(newItem):
    global startPointer, heapStartPointer
    
    if heapStartPointer != nullPointer:
        tempPointer = startPointer
        startPointer = heapStartPointer
        heapStartPointer = DestinationsPointers[heapStartPointer]
        Destinations[startPointer] = newItem
        DestinationsPointers[startPointer] = tempPointer
    
    else:
        print("Linked list full, cannot insert.")

## Subroutine to traverse the linked list and print out its elements
def traverse():
    print("")
    
    global startPointer
    itemPointer = startPointer

    print(Destinations[itemPointer])

    while DestinationsPointers[itemPointer] != nullPointer:
        itemPointer = DestinationsPointers[itemPointer]
        print(Destinations[itemPointer])


# ## TASK 3.5
# Write program code to declare the linked list, using an array.

## Declare constants and variables
startPointer = -1           # INTEGER
heapStartPointer = 0        # INTEGER
nullPointer = -1            # INTEGER CONSTANT

## Arrays of the linked list itself
Destinations = [None for i in range(10)]                # ARRAY[1:10] OF VOID
DestinationsPointers = [(i + 1) for i in range(10)]     # ARRAY[1:10] OF INTEGER
DestinationsPointers[9] = -1

## Insert the given destinations one by one
for Destination in ["Paris, France", "Rome, Italy", "New Delhi, India", "Kuala Lumpur, Malaysia", "Wellington, New Zealand", "New York, USA"]:
    insert(Destination)

## Traverse the linked list and print out each element to test
traverse()

# ## TASK 3.6
# Extend your **program code** by writing a subroutine that adds a new destination to the end of your
# linked list.

# We already implemented this routine and used it to initiaize the linked list. But a copy is given here.

def insert(newItem):
    global startPointer, heapStartPointer
    
    if heapStartPointer != nullPointer:
        tempPointer = startPointer
        startPointer = heapStartPointer
        heapStartPointer = DestinationsPointers[heapStartPointer]
        Destinations[startPointer] = newItem
        DestinationsPointers[startPointer] = tempPointer
    
    else:
        print("Linked list full, cannot insert.")

## Test the routine by adding Reykjavik, Iceland as in TASK 3.3
insert("Reykjavik, Iceland")

## Traverse the linked list and print out each element to test
traverse()

# ## TASK 3.7
# Extend your program code by writing a subroutine to delete the destination node entered by the user from the linked list.

def delete(itemDelete):
    global startPointer, heapStartPointer

    if startPointer == nullPointer:
        print("Linked list empty")
    
    else:
        index = startPointer
        
        while (Destinations[index] != itemDelete) and (index != nullPointer):
            oldIndex = index
            index = DestinationsPointers[index]
        
        if index == nullPointer:
            print("Item", itemDelete, "not found")
        
        else:
            Destinations[index] = None
            tempPointer = DestinationsPointers[index]
            DestinationsPointers[index] = heapStartPointer
            heapStartPointer = index
            DestinationsPointers[oldIndex] = tempPointer

## Delete Kuala Lumpur, Malaysia to test
delete("Kuala Lumpur, Malaysia")

## Traverse the linked list and print out each element to test
traverse()

# ## TASK 3.8
# Discuss other linked list operations that could be implemented.

# Write program code to implement the operation(s) you discuss.

# We already wrote a routine to traverse the linked list and print out elements, but we can write two additional routines:
#   find() to find the given element in the linked list.
#   update() to change the value of an element.

## Procedure to find the given item in the linked list
def find(itemToFind):
    print("")
    
    global startPointer
    itemPointer = startPointer
    index = -1

    if itemToFind == Destinations[itemPointer]:
        index = itemPointer

    while (DestinationsPointers[itemPointer] != nullPointer) and (index == -1):
        itemPointer = DestinationsPointers[itemPointer]
        
        if itemToFind == Destinations[itemPointer]:
            index = itemPointer
    
    if index == -1:
        print(itemToFind + " could not be found in the list.")
    
    return index

## Procedure to update the given item in the linked list
def update(itemToUpdate, newItem):
    index = find(itemToUpdate)

    if index != -1:
        Destinations[index] = newItem

## Print out the list before any updates
traverse()

## Look for New Delhi, India and output the index if it was found
print ("New Delhi, India was found at index " + str(find("New Delhi, India")))

## Look for Bangalore, India and output the index if it was found
find("Bngalore, India")

## Look for New Delhi, India and update it to Bangalore, India if it was found
update("New Delhi, India", "Bangalore, India")

## Print out the list after all updates
traverse()