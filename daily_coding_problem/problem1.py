"""
Given a list of numbers and a number k,
 return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17,
 return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

input_list = [10, 15 ,3 , 7]
k = 18


def test_for_sum(input_list, k):
    return_val = False
    for i, x in enumerate(input_list):
        for j, y in enumerate(input_list):
            if(i != j):
                if(x + y == k):
                    return_val = True
                    return return_val
    return return_val

#the question can be rephrased as 
# given an element of input_list "x"
# does there exist any other element of input_list "y", such that
# y = k - x
#written in this way we can pass through the list once populating a new list 
# and return true if an element is in that list

def test_for_sum2(input_list,k):
    """
    function checks whether any two elements in input_list add to k
    """
    return_val = False
    second_list = []
    for i, x in enumerate(input_list):
        second_list.append(k - x)
        for j, y in enumerate(second_list):
            if (i != j):
                if (x == y):
                    return_val = True
                    return return_val
    return return_val

test_for_sum(input_list,k)
test_for_sum2(input_list,k)

