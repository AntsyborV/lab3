
def calculate_average(num_list):
    """
    Calculate the average of a list of numbers.

    Args:
        num_list (list): List of numbers.

    Returns:
        float: Average value.
    """
    if len(num_list) == 0:
        return None
    return sum(num_list) / len(num_list)

def is_even(number):
    """
    Check if a number is even.

    Args:
        number (int): Number to check.

    Returns:
        bool: True if the number is even, False otherwise.
    """
    return number % 2 == 0

def count_even_numbers(num_list):
    """
    Count the number of even numbers in a list.

    Args:
        num_list (list): List of numbers.

    Returns:
        int: Count of even numbers.
    """
    count = 0
    for number in num_list:
        if is_even(number):
            count += 1
    return count

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6]
    average = calculate_average(numbers)
    print(f"Average: {average}")
    EVEN_COUNT = count_even_numbers(numbers)
    print(f"Number of even numbers: {EVEN_COUNT}")
