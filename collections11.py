Data Structurs:
    * it is group of data items, stored in single memory
    location.
    *Data items can be different types.
    *There are 4 types of collections.
        1.list
        2.set
        3.tuple
        4.dictionary
1.list:
    * used to store group of objects.
    * it allow different type of objects
    * duplicates are allowed
    * list is indexed, each object is identified by using
    index number
        index begins with 0 and ends with length-1
    * you can create a list using two diffrent methods
        1.using []
        syn:
            listname=[item1,item2,...]
        ex:
            colors=["red","green","blue"]
            
        2.using list()
        syn:
            listname=list([item1,item2,...])
        ex:
            colors=list(["red","green","blue"])

    how to access each data item from list?
      data item accessed by using listname along with index
       ex:
           colors=['red','green','blue']
           colors[0]='red'
           colors[1] => 'green'
           colors[2]=> 'blue'
           colors[3]=> IndexError
    modifying item in a list:
        * listname and index is used to modify an item.
    ex:
            colors[0]='RED' # modify old data item
            
    len() used to known the length of list
    
        len(colors) => 3
    del used to delete a list (collection)
        del colors



        
 List Methods:
    append(): used to add item to a list at the end
    ex:
        colors=['red','green','blue']
        colors.append('yellow')
    insert(): used to add an item to a list at selected
    index
    ex:
        colors.insert(1,'white')
    remove(): used to delete an item from list
    ex:
        colors.remove('white')
    clear(): used to remove all items from list
    ex:
        colors.clear()
    sort(): used to arrange elements into ascending or
    descending order
    ex:
        colors.sort() # ascending order
        colors.sort(reverse=True) # descending order
    reverse(): used to reverse the items present in list
    ex:
        colors.reverse()
    count(): used to count element present in list or not.
        ex:
            colors.count('red') # 1
    copy():used to copy one list of items to create new list.
    ex:
        colors1=colors.copy()
    extend(): to add items of list at then end of another list

    ex:
        colors=['red','blue']
        colors1=['green','yellow']
        colors.extend(colors1)
        colors
        ['red','blue','green','yellow']

#program to create a list and read element from user and add it
#to the list

colors=['red','green','blue']
ele=input("Enter your color")
colors.apped(ele)
print(colors)


sets:
    * Set is also collection used to store group of
    objects
    * set allows only unqiue values (No-duplicates)
    * set is created using two ways
        1.using {}
        ex:
              colors={'red','green','blue'}
        2.using set()
        ex:
            colors=set(['red','green','blue'])
    * set is not index like list
    * elements not identified with index
    * Set uses Hashing technique internally.
    * Each object having a key (assigned by system)
    * Set is not updatable like list
    * Set maintains acending order by default.

#convert the following list into set
#print all set elements
x=[4,2,56,6,7,8,5,4,3,3,2,4,5]
x=set(x) #convert x into set -> remove duplicates
print(x) #print set 2,3,4,5,6,7,8,56

#for loop to iterate set elements
for i in x:
    print(i)
    pass

# find and print only even numbers
for i in x:
    if i%2==0:
        print(i)
        pass
    pass


Set methods:

add(): it will add element at the end of set.
ex:
>>>colors={'red','green','blue'}
>>>colors.add('yellow')
>>>colors
{'blue', 'green', 'red', 'yellow'}

clear(): used remove all elements from set
ex:
>>>colors={'red','green','blue'}
>>>colors.clear()
>>>colors
{}

copy(): Used to copy one set items into another set.
ex:
>>>colors={'red','green','blue'}
>>>newcolors=colors.copy()
>>>newcolors
{'blue','green','red'}

union(): it will return all elements from set1 and
non-equalelements from set2 which are not prsent in set1
ex:
>>>num1={1,2,3,4}
>>>num2={3,4,5,6}
>>>num1.union(num2)
{1, 2, 3, 4, 5, 6}

difference(): used to return non-common elements from set1
which are not present in set2
ex:
>>>num1.difference(num2)
{1, 2}

intersection(): it will return only common elements from
both sets.
ex:
>>>num1.intersection(num2)
{3,4}

difference_update(): used to update the set1 by removing
elements from set1 which are present in set2
ex:
>>>num1.difference_update(num2)
>>>num1
{1,2}

intersection_update(): it will update set1 (called-set)
with common elements from both sets.

>>>num1={1,2,3,4}
>>>num2={3,4,5,6}
>>>num1.intersection_update(num2)
>>>num1
{3,4}

remove(): Used to remove an element from set
ex:
>>>nums={2,3,4,5}
>>>nums.remove(2)
>>>nums
{3,4,5}

pop(): it will remove frist element from set.
ex:
>>>nums={1,2,3,4}
>>>nums.pop()
1
>>>nums
{2,3,4}

update(): used to update one set with elements of
another set
ex:
>>>num1={1,2,3,4}
>>>num2={6,7,8,9}
>>>num1.update(num2)
>>>num1
{1,2,3,4,6,7,8,9}
