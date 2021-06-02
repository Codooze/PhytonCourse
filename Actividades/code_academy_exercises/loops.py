#! nested loops
# sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

# scoops_sold = 0

# for location in sales_data:
#     print(location)
#     for element in location:
#         scoops_sold += element
# *print(scoops_sold)


# region #!Loops entry level
# region #! 2. Greetings
# You are invited to a social gathering, but you are tired of greeting everyone there.
# Luckily we can create a function to accomplish this task for us. In this challenge, we will take a list of names
# and prepend the string 'Hello, ' before each name. This will require a few steps:
# endregion

def add_greetings(names):
    new_list = []
    for name in names:
        new_list.append("Hello, " + name)
    return new_list


# *print(add_greetings(["Owen", "Max", "Sophie"]))

# region 3. #!Delete Starting Even Numbers
# Let’s try a tricky challenge involving removing elements from a list. This function will repeatedly remove
# the first element of a list until it finds an odd number or runs out of elements. It will accept a list
# of numbers as an input parameter and return the modified list where any even numbers at the beginning of the
#  list are removed. To do this, we will need the following steps:
# endregion

def delete_starting_evens(lst):
    while (len(lst) > 0 and lst[0] % 2 == 0):
        lst = lst[1:]
    return lst


# After defining our method, we use a while loop to keep iterating as long as some provided conditions are true.
    #  We provide two conditions for the while loop to continue. We will keep iterating as long as there is
    #  at least one number left in the list len(lst) > 0 and if the first element in the list is even
    #  lst[0] % 2 == 0. If both of these conditions are true, then we replace the list with every element
    #  except for the first one using lst[1:]. Once the list is empty or we hit an odd number, the while loop
    #  terminates and we return the modified list.

# ? this funtion that I came up with didn't work on all cases, it prints the 10 even though is an eve number
# ? in the second case
def delete_starting_evens2(lst):
    for number in lst:
        if number % 2 == 0:
            del lst[0]
        else:
            continue
    return lst


# *print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
# *print(delete_starting_evens([4, 8, 10]))

# region #!4. Odd Indices
# This next function will give us the values from a list at every odd index. We will need to accept a list
# of numbers as an input parameter and loop through the odd indices instead of the elements.
# endregion

def odd_indices(lst):
    new_lst = []
    for index in range(1, len(lst), 2):
        new_lst.append(lst[index])
    return new_lst

# The function should create a new empty list and add every element from lst that has an odd index.
# The function should then return this new list.


# ?la funcion de abajo seria si fuera para regresar cada odd number

def odd_indices2(lst):
    new_lst = []
    for number in range(len(lst)):
        if lst[number] % 2 != 0:
            new_lst.append(lst[number])
        else:
            continue
    return new_lst

# *print(odd_indices([4, 3, 7, 10, 11, -2]))


# region #!5. Exponents
# In this challenge, we will be using nested loops in order to raise a list of number to the power of a
#  list of other numbers. What this means is that for every number in the first list, we will raise that number
#   to the power of every number in the second list. If you provide the first list with 2 elements and
#   the second list with 3 numbers, then there will be 6 final answers.
# endregion
def exponents(bases, powers):
    new_list = []
    for base in bases:
        for power in powers:
            new_list.append(base ** power)
    return print(new_list)


#   exponents([2, 3, 4, 5], [2, 3])
# endregion

# region #!Advance loops
# region #!4. Same Values
# Write a function named same_values() that takes two lists of numbers of equal size as parameters.
# The function should return a list of the indices where the values were equal in lst1 and lst2.
# For example, the following code should return [0, 2, 3]
# same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5])
# endregion


def same_values(lst1, lst2):
    new_lst = []
    for index in range(len(lst1)):
        if lst1[index] == lst2[index]:
            new_lst.append(index)
    return new_lst


# *print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))
# In this solution, we used a loop that iterates using the range of the len of our list. This generates the indices we need to iterate through.
#  Note that we assume the lists are of equal size. We then access the element at the current index from each list using lst1[index] and lst2[index].
#  If they are equal we add the index to the new list. Finally, we return the results.

# region #!5. Reversed List
# For the final challenge, we are going to test two lists to see if the second list is the reverse of the first list.
#  There are a few different ways to approach this, but we are going to try a method that iterates through each of the values in one direction
#   for the first list and compares them against the values starting from the other direction in the second list.
# For example, reversed_list([1, 2, 3], [3, 2, 1]) should return True.
# endregion


def reversed_list(lst1, lst2):
    for index in range(len(lst1)):
        print("len:", len(lst2), end="  index_value: ")
        print(lst2[len(lst2)-1-index])
        if lst1[index] != lst2[len(lst2) - 1 - index]:
            return False
    return True

# *print(reversed_list([1, 5, 3], [3, 4, 1]))
# *print(reversed_list([1, 2, 3], [3, 2, 1]))
# That math is a little complicated — it helps to look at a concrete example. If we are given a list of 5 elements,
# the valid indices are 0 to 4. Because of this, the last index in the second list is len(lst2) - 1, or 5 - 1 = 4.
# Now in order to get the inverse of the position we are at in the first list, we subtract the index we are at from
# the end of the second list. So on the first pass, we’ll compare the element at position 0 to the element at position
#  5 - 1 - 0 = 4. On the next pass, we’ll compare the element at position 1 to the element at position 5 - 1 - 1 = 3,
#  and so on  You could also try simplifying this code by using the python function reversed() or other methods such
#  as ‘slicing’..
# endregion
