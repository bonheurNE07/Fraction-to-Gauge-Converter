def main():
    """
    Main function to take input from the user, convert the fraction,
    and print the gauge value.
    """
    fraction = input("Fraction: ")
    try:
        percentage = convert(fraction)
        result = gauge(percentage)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

def convert(fraction: str) -> int:
    """
    Converts a fraction string to a percentage integer.

    Parameters:
    fraction (str): The fraction as a string in the form 'x/y'.

    Returns:
    int: The fraction as a percentage rounded to the nearest integer.

    Raises:
    ValueError: If the input is not a valid fraction or if the numerator
                is greater than the denominator.
    ZeroDivisionError: If the denominator is zero.
    """
    try:
        x, y = map(int, fraction.split("/"))
    except ValueError:
        raise ValueError("Fraction must be in the form 'x/y' where x and y are integers.")

    if y == 0:
        raise ZeroDivisionError("Denominator cannot be zero.")

    if x > y:
        raise ValueError("Numerator cannot be greater than denominator.")

    return round((x / y) * 100)

def gauge(percentage: int) -> str:
    """
    Converts a percentage integer to a gauge string.

    Parameters:
    percentage (int): The percentage as an integer.

    Returns:
    str: The gauge value as a string.
    """
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()