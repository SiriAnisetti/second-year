def check_even_odd(num):
    """
    Function to check if a number is even or odd.
    Args:
    num (int): The number to check.

    Returns:
    None
    """
    try:
        # Check if the number is even
        if num % 2 == 0:
            print(f"{num} is even")
        # If not even, then it's odd
        else:
            print(f"{num} is odd")
    except TypeError:
        # Handle the exception if input is not an integer
        print("Please enter a valid integer.")

    if num % 2 ==0:  
        print(f"{num} is even")
    else:
        print(f"{num} + is odd") 
    if num % 2 == 0:  
        print(f"{num} is even")
    else:
        print("is odd")
    return None

check_even_odd(7) 
check_even_odd(-4)  
