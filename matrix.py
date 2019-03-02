#This is a simple OOP matrix implementation
import numbers
#test inputs

# parse into a column
test_input1 = [1,2,3,4,5,6,7,8,9]
# parse into a matrix with the three sub lists the rows
test_input2 = [[1,2,3],[4,5,6],[7,8,9]]
#reject as data is wrong shape
test_input3 = [[[1,2],[3,4]],[[5,6],[7,8]]]
#reject as rows of inconsistent length
test_input4 = [[1,2,3],[4,5],[7,8,9]]
#reject as not all elements are numeric
test_input5 = [1,2,"a"]

class Matrix:
    """
    This class creates a simple matrix as an experiment in oop
    """
    def __init__(self, input_list):
        """
        Initialise the matrix from a list - can be a nested listed up to two deep
        These matrices will be stored as a nested list and will have methods to access them like a matrix
        """
        self.input_list = input_list
        
        try:
            self.matrix = self.handle_input()

    def handle_input(self):
        """
        This function takes an input_list and shapes it into the required two level structure
        This function also includes error handling for unsupported data types and list shapes
        """
        #need to check that the object is a list
        if type(self.input_list) != list:
            raise TypeError("object must be a list")
        #need to check that there are 1 or two levels of nested lists
        #need to check that all objects are of type numeric
        for i in self.input_list:
            if isinstance(i, numbers.Number) != True:
                raise TypeError("all elements must be numeric")
        #need to check that all 2nd level sublists are of same length



    def print_matrix(self):
        """
        print the matrix to the console
        """
        pass


    def print_dims(self):
        """
        print the dimensions of the matrix
        """
        pass

    def select_column(self):
        """
        select a single column by index and return as a list
        """
        pass

    def select_row(self):
        """
        select a single row by index and return as a list
        """
        pass

    def select_element(self):
        """
        select a single element of the matrix and return as a list
        """
        pass


def test_matrix(input_file):
    """
    simple test function for the Matrix class
    """
    try:
        output = Matrix(input)
        print("pass")
    except:
        print("fail")
    
#pass
print("test1")
test_matrix1 = test_matrix(test_input1)
#pass
print("test2")
test_matrix2 = test_matrix(test_input2)
#fail
print("test3")
test_matrix3 = test_matrix(test_input3)
#fail
print("test4")
test_matrix4 = test_matrix(test_input4)
#fail
print("test5")
test_matrix5 = test_matrix(test_input5)

test_matrix1.print_matrix()
test_matrix2.print_matrix()

