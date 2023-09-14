from DynamicList.myList import MyList

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')

    my_list = MyList()
    my_list.append(3)
    my_list.append(1)
    my_list.append(4)
    my_list.append(6)
    my_list.append(7)
    my_list.append(2)
    my_list.append(5)
    print(my_list)
    print(f"Min Value is : {min(my_list)}")
    print(f"Max Value is : {max(my_list)}")

    print("-----"*10)

    char_list = MyList()
    char_list.append("b")
    char_list.append("z")
    char_list.append("A")
    char_list.append("c")
    print(char_list)
    print(f"Min Value is : {min(char_list)}")
    print(f"Max Value is : {max(char_list)}")