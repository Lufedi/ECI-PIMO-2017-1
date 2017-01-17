__author__ = 'luisfediaz'


#Constant
def func_constant(values):
    '''
    Prints first item in a list of values.
    '''
    print(values[0])

func_constant([1,2,3])


#Linear
def func_lin(lst):
    '''
    Takes in list and prints out all values
    '''
    for val in lst:
        print (val)

func_lin([1,2,3])


#Cuadratic
def func_quad(lst):
    '''
    Prints pairs for every item in list.
    '''
    for item_1 in lst:
        for item_2 in lst:
            print (item_1,item_2)

lst = [0, 1, 2, 3]

func_quad(lst)



#Scale
def print_3(lst):
    '''
    Prints all items three times
    '''
    for val in lst:
        print (val)

    for val in lst:
        print (val)

    for val in lst:
        print (val)



def comp(lst):
    '''
    This function prints the first item O(1)
    Then is prints the first 1/2 of the list O(n/2)
    Then prints a string 10 times O(10)
    '''
    print (lst[0])

    midpoint = len(lst)/2

    for val in lst[:midpoint]:
        print (val)

    for x in range(10):
        print ('number')



#Scape Complexity
def printer(n=10):
    '''
    Prints "hello world!" n times
    '''
    for x in range(n):
        print ('Hello World!')

def create_list(n):
    new_list = []

    for num in range(n):
        new_list.append('new')

    return new_list

