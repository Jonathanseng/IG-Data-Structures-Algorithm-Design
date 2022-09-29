# Defition of the array: In computer science, an array is a data structure consisting of a collection of elements, each identified by at least one array index or key. An array is stored such that the position of each element can be computed from its index tuple by a mathematical formula.
# In creating the array in any programming language the different is just the syntax

# when you do need to use the array? In programming, most of the cases need to store a large amount of data of a similar type. We need to define numerous variables to store such a huge amount of data. While writing the programs, it would be very tough to memorize all variable names. Instead, it is better to define an array and store all the elements in it. The following example illustrates how an array can be used while writing a code- In the following example, we have given marks to a student in 5 different subjects. The aim is to calculate the average of a student’s marks.
# Usually the creating of the array in python we will have the name = [] -> the bracket sign

array = []

# Here are the operation on the array 
# Method 	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

# let add some element inside the empty array ~ there are 2 ways for inserting the data into the array. 1 is adding to the end of the array we use the append and 2. we use the insert keyworks (built in function for the array in python) 
array.append(1)
array.insert(10, 0) # in the bracket 0 is the position and second parameter is the value
