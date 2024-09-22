"""
Module for checking answers from excercises.

"""
import numpy as np

""" Checking answers from numpy excercises"""

def arrays_equal(arr1, arr2):
    return np.array_equal(arr1, arr2)

# Function to reveal solutions
def answer(function_name):
    solutions = {
        'exercise1': "np.arange(10)",
        'exercise2': "np.full((3, 3), True, dtype=bool)",
        'exercise3': "arr3[arr3 % 2 == 1]",
        'exercise4': "arr4[arr4 % 2 == 1] = -1",
        'exercise5': "arr5.reshape(2, -1)",
        'exercise6': """np.random.seed(0)
                        arr6 = np.random.random((5, 5))
                        min_value = arr6.min()
                        max_value = arr6.max()""",
                                'exercise7': "np.random.uniform(5, 10, size=(5, 3))",
                                'exercise8': """np.random.seed(0)
                        arr8 = np.random.randint(1, 101, 10)
                        arr8_sorted = np.sort(arr8)""",
                                'exercise9': "np.eye(3)",
                                'exercise10': """np.random.seed(0)
                        arr10 = np.random.randint(1, 11, size=(5, 5))
                        row_sums = np.sum(arr10, axis=1)
                        col_sums = np.sum(arr10, axis=0)"""
    }
    print(f"Solution for {function_name}:")
    print(solutions.get(function_name, "Solution not found."))

def check_exercise1(arr1):
    solution1 = np.arange(10)
    print("Correct!" if arrays_equal(arr1, solution1) else "Try again. Use answer('exercise1') to see the solution.")


def check_exercise2(arr2):
    solution2 = np.full((3, 3), True, dtype=bool)
    print("Correct!" if arrays_equal(arr2, solution2) else "Try again. Use answer('exercise2') to see the solution.")

def check_exercise3(odd_numbers):
    arr1 = np.arange(10)
    solution3 = arr1[arr1 % 2 == 1]
    print("Correct!" if arrays_equal(odd_numbers, solution3) else "Try again. Use answer('exercise3') to see the solution.")

def check_exercise4(arr4):
    solution4 = np.array([0, -1, 2, -1, 4, -1, 6, -1, 8, -1])
    print("Correct!" if arrays_equal(arr4, solution4) else "Try again. Use answer('exercise4') to see the solution.")

def check_exercise5(arr5_2d):
    arr5 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    solution5 = arr5.reshape(2, -1)
    print("Correct!" if arrays_equal(arr5_2d, solution5) else "Try again. Use answer('exercise5') to see the solution.")


def check_exercise6(arr6,):
    np.random.seed(0)
    min_value=arr6.min()
    max_value=arr6.max()
    print("Array is correct!" if arr6.shape == (5,5) else "Array is incorrect. Try again.")
    print("Minimum value is correct!" if min_value == arr6.min() else f"Minimum value is incorrect.")
    print("Maximum value is correct!" if max_value == arr6.max() else f"Maximum value is incorrect.")
    if not (arr6.shape == (5,5) and min_value == arr6.min() and max_value == arr6.max()):
        print("Use answer('exercise6') to see the solution.")


def check_exercise7(arr7):
    np.random.seed(0)
    solution7 = np.random.uniform(5, 10, size=(5, 3))
    print("Correct!" if arrays_equal(arr7, solution7) else "Try again. Use answer('exercise7') to see the solution.")


def check_exercise8(arr8, arr8_sorted):
    np.random.seed(0)
    solution8 = np.random.randint(1, 101, 10)
    solution8_sorted = np.sort(solution8)
    print("Original array is correct!" if arrays_equal(arr8, solution8) else "Original array is incorrect.")
    print("Sorted array is correct!" if arrays_equal(arr8_sorted, solution8_sorted) else "Sorted array is incorrect.")
    if not (arrays_equal(arr8, solution8) and arrays_equal(arr8_sorted, solution8_sorted)):
        print("Use answer('exercise8') to see the solution.")


def check_exercise9(identity_matrix):
    solution9 = np.eye(3)
    print("Correct!" if arrays_equal(identity_matrix, solution9) else "Try again. Use answer('exercise9') to see the solution.")

def check_exercise10(arr10, row_sums, col_sums):
    np.random.seed(0)
    solution10 = np.random.randint(1, 11, size=(5, 5))
    solution_row_sums = np.sum(solution10, axis=1)
    solution_col_sums = np.sum(solution10, axis=0)
    print("Array is correct!" if arrays_equal(arr10, solution10) else "Array is incorrect.")
    print("Row sums are correct!" if arrays_equal(row_sums, solution_row_sums) else "Row sums are incorrect.")
    print("Column sums are correct!" if arrays_equal(col_sums, solution_col_sums) else "Column sums are incorrect.")
    if not (arrays_equal(arr10, solution10) and arrays_equal(row_sums, solution_row_sums) and arrays_equal(col_sums, solution_col_sums)):
        print("Use answer('exercise10') to see the solution.")
