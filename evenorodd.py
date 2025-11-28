def evenorodd(number):
    """Determine if a number is even or odd.

    Args:
        number (int): The number to check.
    Returns:
        str: "Even" if the number is even, "Odd" if the number is odd.
    """
    if (number % 2) == 0:
        return "Even"
    else:
        return "Odd"    
    

# Example usage
#num = 7 # You can change this value to test with other numbers
#result = evenorodd(num)
number=int(input("Enter a number to check if it is even or odd: "))
result=evenorodd(number)
print(f"The number {number} is {result}.")

