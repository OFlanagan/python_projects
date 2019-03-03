#This is a simple OOP matrix implementation
import numbers
#test inputs

class Matrix:
    """
    This class creates a simple matrix as an experiment in oop
    """
    def __init__(self, input_list):
        """
        Initialise the matrix from a list - can be a nested listed up to two deep
        These matrices will be stored as a nested list and will have methods to access them like a matrix
        """
        self.matrix = self.handle_input(input_list)
        self.dims = self.get_dims()


    def handle_input(self, input_list):
        """
        This function takes an input_list and shapes it into the required two level structure
        This function also includes error handling for unsupported data types and list shapes
        """

        #need to check that the object is a list
        if type(input_list) != list:
            raise TypeError("object must be a list")
        if len(input_list) < 1:
            raise ValueError("list must have an element")
        #need to check that there are 1 or two levels of nested lists
        #need to check that all objects are of type numeric
        #we can check these at the same time
        #we check the type of the first element and see if it is a list or a
        #numeric
        if type(input_list[0]) == list:
            # if it is a list then we record the length of the list and ensure
            # that all elements of input_list are lists of the same length as the 
            #first list
            list_len = len(input_list[0])
            #at this stage we have established that the first element of the
            #input list is a list, so we need to check that all list elements
            # are lists of the same length as the first element
            # we also need to check that the elements of each list are all numeric
            for i in input_list:
                if type(i) != list:
                    raise TypeError("all elements of a nested list must be lists")
                if len(i) != list_len:
                    raise ValueError("all elements of a nested list must be"\
                    "of same length")
                for j in i:
                    if isinstance(j, numbers.Number) != True:
                        raise TypeError("all elements of sublists must be numeric")
            #if the input list passes our tests, it satisfies the requirements
            #for our matrix and so we will just use it as our matrix
            return input_list

        elif isinstance(input_list[0], numbers.Number) == True:
            #if our input list is a list of numbers we will create it as a sublist
            return_list = [[]]
            for i in input_list:
                if isinstance(i, numbers.Number) != True:
                    raise TypeError("all elements must be numeric")
                else:
                    return_list[0].append(i)
            return return_list
        else:
            raise TypeError("A matrix must be made up of a list of numbers," \
            "or a list of list of numbers")
        # if it is numeric then all elements of the list must be numeric




    def print_matrix(self):
        """
        print the matrix to the console
        this function provides no return and is called soley for its side effects
        """
        for i in self.matrix:
            for j in i:
                print(f"{j} ",end="")
            print("")
        print("")


    def get_dims(self):
        """
        this function returns a list with the [number of rows, number of cols]
        """
        return [len(self.matrix), len(self.matrix[0])]

    def print_dims(self):
        """
        print the dimensions of the matrix
        """
        print(f"{self.dims[0]} rows, {self.dims[1]} columns")
        print()

    def select_column(self, col_index):
        """
        select a single column by index and return as a list
        """
        column = []
        for row in self.matrix:
            column.append(row[col_index])
        return column
    def select_row(self, row_index):
        """
        select a single row by index and return as a list
        """
        return self.matrix[row_index]

    def select_element(self, row_index, col_index):
        """
        select a single element of the matrix and return as a list
        """
        return self.matrix[row_index][col_index]


def matrix_add(matrix1, matrix2):
    """
    This function performs basic matrix addition on two matrices of the same 
    size
    """
    #need to check that both objects are matrices
    if isinstance(matrix1, Matrix) and isinstance(matrix2, Matrix) != True:
        raise TypeError("both inputs must be of class matrix")
    #need to check that both matrices are the same size
    if matrix1.dims != matrix2.dims:
        raise ValueError("both inputs must be of the same size")
    #need to add the contents
    for r_ind, row in enumerate(matrix1.matrix):
        for c_ind, col in enumerate(row):
           matrix1.matrix[r_ind][c_ind] += matrix2.matrix[r_ind][c_ind]
    return matrix1

def matrix_multiplication(matrix1, matrix2):
    """
    This function performs matrix multiplication ont two matrices
    """
    #need to make sure both inputs are matrices
    if isinstance(matrix1, Matrix) and isinstance(matrix2, Matrix) != True:
        raise TypeError("both inputs must be of class matrix")

    #need to make sure that the two matrices are compatible
    #i.e. the number of columns of matrix 1 equal the number of rows 
    #of matrix 2
    if matrix1.dims[1] != matrix2.dims[0]:
        raise ValueError("the number of columns of input1 must equal the"\
        "number of rows of input2")
    #TODO

def test_matrix(input_list):
    """
    simple test function for the Matrix class
    """
    try:
        output = Matrix(input_list)
        print("pass")
        return output
    except:
        print("fail")


#tests
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


#pass
print("test1")
test_matrix1 = test_matrix(test_input1)
tm1 = Matrix(test_input1)
#pass
print("test2")
test_matrix2 = test_matrix(test_input2)
tm2 = Matrix(test_input2)
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
test_matrix2.print_dims()
test_matrix2.print_matrix()
test_matrix1.print_dims()

print(test_matrix1.select_column(4))
print(test_matrix1.select_column(8))
print(test_matrix1.select_row(0))
print(test_matrix2.select_column(2))
print(test_matrix2.select_row(2))
print(test_matrix1.select_element(0,1))
try:
    test_add_matrix = matrix_add(tm1, tm2)
except:
    print("fail")

print("Testing additions")
test_add_matrix1 = matrix_add(tm1, tm1)
test_add_matrix1.print_matrix()
test_add_matrix2 = matrix_add(tm2, tm2)
test_add_matrix2.print_matrix()



