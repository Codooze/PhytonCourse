# region ListEntryLevel
# region 4. More Than N
# Our factory produces a variety of different flavored snacks and we want to check the number of instances of
# a certain type. We have a conveyor belt full of different types of snacks represented by different numbers.
#  Our function will accept a list of numbers(representing the type of snack),
#  a number for the second parameter(the type of snack we are looking for),
#  and another number as the third parameter(the maximum number of that type of snack on the conveyor belt).
# The function will return True if the snack we are searching for appears more times than we provided as our
# third parameter. These are the steps we need:

# Define the function to accept three parameters, a list of numbers, a number to look for, and a number for the number of instances
# Count the number of occurrences of item(the second parameter) in lst(the first parameter)
# If the number of occurrences is greater than n(the third parameter), return True. Otherwise, return False
# endregion
def more_than_n(lst, item, n):
    if lst.count(item) > n:
        return True
    else:
        return False


#print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))


# region 2. Append Sum
# Let’s create a function that calculates the sum of the last two elements of a list and appends it to the end.
# After doing so, it will repeat this process two more times and return the resulting list. You can choose to use
# a loop or manually use three lines. Here are the steps we need:

# Define the function to accept one parameter for our list of numbers
# Add the last and second to last elements from our list together
# Append the calculated value to the end of our list.
# Repeat steps 2 and 3 two more times
# Return the modified list
# endregion

def append_sum(lst):
    for i in range(3):
        lst.append(lst[-1]+lst[-2])
    return lst


#print(append_sum([1, 1, 2]))


# region 3. Larger List
# Let’s say we are working with two conveyor belts that contain items represented by a numerical ID.
# If one conveyor belt contains more items than the other, then we need to return the ID of the last item on that belt.
#  In the case where they have the same number of items, return the last item from the first conveyor belt.
#  In our code, we can represent the belts using lists. Here are the steps:

# Define the function to accept two parameters for our two lists of numbers
# Check if the length of the first list is greater than or equal to the length of the second list
# If true, then return the last element from the first list. Otherwise, return the last element from the second list
# endregion

def larger_list(lst1, lst2):
    if len(lst1) >= len(lst2):
        return lst1[-1]
    else:
        return lst2[-1]


#print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))


# region 5. Combine Sort
# Finally, let’s create a function that combines two different lists together and then sorts them.
# To do this we can combine the lists with an operation and then sort using a function call.
#  Here are the steps we need to use:
# endregion

def combine_sort(lst1, lst2):
    unsorted = lst1 + lst2
    sorted_list = sorted(unsorted)
    return sorted_list


#print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
# endregion

# region ListAdvance
# region #!1. Every Three Numbers
# Let’s start our challenging problems with a function that creates a list of numbers up to 100 in increments
#  of 3 starting from a number that is passed to the function as an input parameter. Here is what we need to do:
# endregion
def every_three_nums(start):
    return list(range(start, 101, 3))


# * print(every_three_nums(91))

# region #!2. Remove Middle
# Our next function will remove all elements from a list with an index within a certain range.
# The function will accept a list, a starting index, and an ending index. All elements with an index between
#  the starting and ending index should be removed from the list. Here are the steps:
# endregion

def remove_middle(lst, start, end):
    return lst[:start] + lst[end+1:]


# *print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))


# para entender lo de arriva

def list_slicing():
    a = [1, 2, 3, 4, 5]
    start = a[:3]
    end = a[1+1:]
    print(start)
    print(end)


# *list_slicing()

# region #!4. Double Index  !!!
# Our next function will double a value at a given position. We will provide a list and an index to double.
# This will create a new list by replacing the value at the index provided with double the original value.
#  If the index is invalid then we should return the original list. Here is what we need to do:
# endregion


def double_index(lst, index):
    if index >= len(lst):
        return lst
    else:
        # Gets the original list up to index
        new_lst = lst[0:index]  # hew index is not inclusive
        print(new_lst)  # for degugging
 # Adds double the value at index to the new list
        new_lst.append(lst[index]*2)
        print(new_lst)  # for debugging
        print(lst[index+1:])  # for debugging
  #  Adds the rest of the original list
        new_lst = new_lst + lst[index+1:]
        return new_lst


# Uncomment the line below when your function is done
#print(double_index([3, 8, -10, 12], 2))

# region #!5. Middle Item
# For the final code challenge, we are going to create a function that finds the middle item from a list of values.
# This will be different depending on whether there are an odd or even number of values.
#  In the case of an odd number of elements, we want this function to return the exact middle value.
#  If there is an even number of elements, it returns the average of the middle two elements.
#   Here is what we need to do:
# Define the function to accept one parameter for our list of numbers
# Determine if the length of the list is even or odd
# If the length is even, then return the average of the middle two numbers
# If the length is odd, then return the middle number
# endregion


def middle_element(lst):
    if len(lst) % 2 == 0:
        sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]
        return sum / 2
    else:
        return lst[int(len(lst)/2)]


# *print(middle_element([5, 2, -10, -4, 4, 5]))
# Note that the math to find the middle index is a bit tricky. In some cases, when we divide by 2,
    # we would get a double. For example, if our list had 3 items in it, then 3/2 would give us 1.5.
    # The middle index should be 1, so in order to go from 1.5 to 1, we cast 1.5 as an int. In total,
    # this is int(len(lst)/2).
# endregion
