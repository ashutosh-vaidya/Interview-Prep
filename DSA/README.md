# Data Structures and algorithms

----

### What are the data structures?

**Data Structures** are way to store and organize the data **efficiently** with respect to time and space complexity.

**[From wikipedia](https://en.wikipedia.org/wiki/Data_structure)**: In computer science, a **data structure** 
is a data organization, management, and storage format that is usually chosen for efficient access to data. 
More precisely, a data structure is a collection of data values, the relationships among them, and the functions 
or operations that can be applied to the data, i.e., it is an algebraic structure about data.

Different types of data structures are suited to different kinds of applications, and some are highly specialized 
to specific tasks. For example, **relational databases** commonly use **B-tree indexes** for data retrieval,
while **compiler** implementations usually use **hash tables** to look up identifiers.

### Examples:

- Social Networking site (Suggest a Friend) : **Graphs**
- File Handling (Undo/Redo) : **Stack** 
- Operating system (drive structure) : **Trees**

### Important Data Structures

- Array
- Linkedlist
- Stack
- Queue
- HashMap/HashTable
- Tree
- Graph

----

## Arrays

**An array** is a linear data structure used to store multiple homogenous (same type) in a continuous memory 
locations. Array are commonly referred as **Call by Value** types.

### Disadvantages of array
1. Fixed size (Memory Wastage)
2. Homogenous Type (Less Flexibility)

To solve this disadvantages there are further two enhanced version of arrays:

### 1. Referential Array

Referential array solves the second issue, i.e. homogenous types. Here, instead of saving the values directly in the
continuous memory locations they are store randomly and the address to their memory location is then stored in the
continuous memory. Since we are saving the address which are numeric we have no issue with saving heterogeneous types
in the respective address.

#### Drawbacks 
1. Extra memory is required
2. Relatively slower than simple array since there is added step to retrieve the values.

### 2. Dynamic Array (IMP)

Dynamic arrays start with the static size but resizes as soon as original capacity is fulled and user tries to add
additional elements. Dynamic arrays are also referential in nature and thus solve both of the drawbacks of array.

**Python's list** are created using dynamic array hence it can save heterogeneous elements.

[Implementation of Dynamic List](https://github.com/ashutosh-vaidya/Interview-Prep/tree/main/DSA/DynamicList)

----

## Linked List



