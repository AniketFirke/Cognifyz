def generate_number_pyramid(rows):
    """
    Generate and print a pyramid number pattern.

    Example for rows=5:
        1
       121
      12321
     1234321
    123454321
    """
    for i in range(1, rows + 1):
        # Create leading spaces
        spaces = ' ' * (rows - i)
        # Create the ascending numbers
        ascending = ''.join(str(j) for j in range(1, i + 1))
        # Create the descending numbers
        descending = ''.join(str(j) for j in range(i - 1, 0, -1))
        # Combine spaces, ascending, and descending numbers
        print(spaces + ascending + descending)

if __name__ == "__main__":
    rows = 5  # You can change the number of rows for the pyramid
    generate_number_pyramid(rows)
