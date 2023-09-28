#!/usr/bin/python3
'''Module to find Pascal's Triangle integers'''

def pascal_triangle(n):
    '''
    Function to find Pascal's Triangle integers

    Parameters:
        n (int): The number of row's of Pascal's triangle

    Returns:
        pascal_triangle (list): Binary string of the sum of a and b
    '''

    # Create an empty list to store Pascal's Triangle rows
    pascal_triangle = list()

    # Check if n is less than or equal to 0
    if n <= 0:
        return pascal_triangle  # Return an empty list if n is not positive

    # Add the first row of Pascal's Triangle, which contains only one element (1)
    if n > 0:
        pascal_triangle.append([1])

    # Add the second row of Pascal's Triangle, which contains two elements (1, 1)
    if n > 1:
        pascal_triangle.append([1, 1])

    # Generate the remaining rows of Pascal's Triangle
    for x in range(3, n+1):
        # Create a new row filled with zeros
        pascal_triangle.append([0] * x)

        # Set the first and last elements of the current row to 1
        pascal_triangle[x-1][0] = 1
        pascal_triangle[x-1][x-1] = 1

        # Calculate the middle numbers in the current row
        for y in range(1, x-1):
            pascal_triangle[x-1][y] = \
                pascal_triangle[x-2][y-1] + pascal_triangle[x-2][y]

    # Return the complete Pascal's Triangle as a list of lists
    return pascal_triangle

