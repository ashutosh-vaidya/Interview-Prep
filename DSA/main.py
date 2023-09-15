#from DynamicList.myList import MyList
from LinkedList.linkedList import LinkedList

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Linked list

    print("Creating a linkedlist")
    ll = LinkedList()
    print(f"No of nodes = {len(ll)}")
    print(ll)

    print("inserting at head")
    ll.insert_head(1)
    ll.insert_head(3)
    ll.insert_head(5)
    print(f"No of nodes = {len(ll)}")
    print(ll)

    print("inserting at tail")
    ll.append(7)
    ll.append("hello")
    print(f"No of nodes = {len(ll)}")
    print(ll)

    print("inserting after (1)")
    ll.insert_after(1, 2)
    print(f"No of nodes = {len(ll)}")
    print(ll)

    print("inserting after (tail)")
    ll.insert_after("hello", "world")
    print(f"No of nodes = {len(ll)}")
    print(ll)

    print("inserting after (single item linkedlist)")
    new_ll = LinkedList()
    new_ll.append(1)
    new_ll.insert_after(1, 2)
    print(f"No of nodes = {len(new_ll)}")
    print(new_ll)

    #following code should throw error
    #print("inserting after (empty linkedlist)")
    #new_ll = LinkedList()
    #new_ll.insert_after(1, 1)

    #print("inserting after (value does not exist)")
    #ll.insert_after(100, 200)
    #print(f"No of nodes = {len(ll)}")
    #print(ll)

    print("inserting before (single item linkedlist/inserting at head)")
    new_ll = LinkedList()
    new_ll.append(1)
    new_ll.insert_before(1, 2)
    print(f"No of nodes = {len(new_ll)}")
    print(new_ll)

    print("inserting before (1)")
    ll.insert_before(1, 0)
    print(f"No of nodes = {len(ll)}")
    print(ll)

    print("inserting before (tail)")
    ll.insert_before("world","again")
    print(f"No of nodes = {len(ll)}")
    print(ll)

    # following code should throw error
    #print("inserting before (empty linkedlist)")
    #new_ll = LinkedList()
    #new_ll.insert_before(1, 1)

    #print("inserting before (value does not exist)")
    #ll.insert_before(100, 200)
    #print(f"No of nodes = {len(ll)}")
    #print(ll)

    print(f"Before head => {ll.head.data}")
    print(f"No of nodes = {len(ll)}")
    print(ll)
    print("Removing head")
    ll.delete_head()
    print(f"After head => {ll.head.data}")
    print(f"No of nodes = {len(ll)}")
    print(ll)

    #print("Before Clearing ll")
    #print(f"ll - {ll}")
    #ll.clear()
    #print("after clearing ll")
    #print(f"ll - {ll}")

    # Dynamic List

    #my_list = MyList()
    #my_list.append(3)
    #my_list.append(1)
    #my_list.append(4)
    #my_list.append(6)
    #my_list.append(7)
    #my_list.append(2)
    #my_list.append(5)
    #print(my_list)
    #print(f"Min Value is : {min(my_list)}")
    #print(f"Max Value is : {max(my_list)}")

    #print("-----"*10)

    #char_list = MyList()
    #char_list.append("b")
    #char_list.append("z")
    #char_list.append("A")
    #char_list.append("c")
    #print(char_list)
    #print(f"Min Value is : {min(char_list)}")
    #print(f"Max Value is : {max(char_list)}")