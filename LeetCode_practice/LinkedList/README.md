# 链表笔记
***
链表（Linked List) 是一种常见的基础数据结构，是一种线性表，但是并不会按线性的顺序存储数据，而是在每一个节点里存到下一个节点的指针（Pointer）。
- 由于不必须按顺序存储，链表在插入的时候可以达到O(1)的复杂度，比另一种线性表——顺序表快得多，但是查找一个节点或者访问特定编号的节点，则需要O(x)的时间，而顺序表相应的时间复杂度分别为O(logn)和O(1)。
- 使用链表结构可以克服数组链表需要预先知道数据大小的缺点，链表结构可以充分利用计算机内存空间，实现灵活的内存动态管理。但是链表失去了数组随机读取的优点，同时链表由于增加了节点的指针域，空间开销比较大。
- 在计算机科学中，链表作为一种基础的数据结构可以用来生成其他类型的数据结构。链表通常由一连串节点组成，每个节点包含任意的实例数据(data fields)和一或两个用来指向上一个/或下一个节点的位置的链接(lines)。
- 链表最明显的好处就是，常规数据排列关联项目的方式可能不同于这些数据项目在记忆体或磁盘上顺序，数据的访问往往要在不同的排列顺序中转换。而链表是一种自我指示数据类型，因为它包含指向另一个相同类型的数据的指针（链接）。
- 链表允许插入和移除表上任意位置的节点，但是不允许随机存取。链表由很多种不同的类型：单向链表，双向链表和循环链表。
- 链表通常可以衍生出循环链表，静态链表，双链表等。对于链表使用，需要注意头节点的使用。
***
### 链表表示
```
#Definition for Linked List 
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
```
***
### 链表的笔记地址
- python 常用算法学习（4）
    — Python常用算法学习（4）——数据结构
    - 地址： https://www.cnblogs.com/wj-1314/p/11574277.html
    
***
###  数组和链表的区别
- 下面学习一下数组和链表的区别，作为线性表的两种存储方式，他们有各自的优缺点。
#### 数组
- 所有元素都连续的存储于一段内存中，且每个元素占用的内存大小相同，这使得数组具备了通过下标快速访问数据的能力。
- 但是连续存储的缺点也很明显，增加容量，增删元素的成本很高，时间复杂度均为O(n)
- 增加数组容量需要先申请一块新的内存，然后复制原有的元素。如果需要的话，可能还要删除原先的内存。
- 删除元素时需要移动被删除元素之后的所有元素以保证所有元素是连续的，增加元素时需要移动指定位置及之后的所有元素，然后将新增元素插入到指定位置，如果容量不足的话，还需要进行扩容操作。
-数组的优缺点：
    - 优点：可以根据偏移实现快速的随机读写
    - 缺点：扩容，增删元素极慢
#### 链表
- 由若干个结点组成，每个结点包含数据域和指针域。
- 一般来说，链表中只会有一个结点的指针域为空，该节点为尾结点，其他结点的指针域都会存储一个节点的内存地址，链表中也只会有一个节点的内存地址没有存储在其他结点的指针域，该节点称为头结点。
- 链表的存储方式使得它可以高效的在指定位置插入与删除，时间复杂度为O（1），在节点 p 之后增加一个节点 q 总共分三步：
    - 1，申请一段内存用以存储 q（可以使用内存池避免频繁申请和销毁内存）
    - 2，将p的指针域数据复制到 q的指针域
    - 3，更新p的指针域为 q 的地址
- 删除结点 p 之后的节点 q 总共分为两步：
    - 将 q 的指针域复制到 p 的指针域
    - 释放 q 节点的内存