startPointer = -1
heapStartPointer = 0
nullPointer = -1

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

def traverse():
    print("")
    
    global startPointer
    itemPointer = startPointer

    print(Destinations[itemPointer])

    while DestinationsPointers[itemPointer] != nullPointer:
        itemPointer = DestinationsPointers[itemPointer]
        print(Destinations[itemPointer])

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

Destinations = [None for i in range(10)]
DestinationsPointers = [(i + 1) for i in range(10)]
DestinationsPointers[9] = -1

for Destination in ["Paris, France", "Rome, Italy", "New Delhi, India", "Kuala Lumpur,  Malaysia", "Wellington, New Zealand", "New York, USA"]:
    insert(Destination)

traverse()

insert("Reykjavik, Iceland")

traverse()

delete("Rome, Italy")

traverse()