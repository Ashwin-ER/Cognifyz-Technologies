def print_star_pyramid(rows):
    # Outer loop for number of rows
    for i in range(1, rows + 1):
        # Print spaces before stars
        for j in range(rows - i):
            print(" ", end=" ")

        # Print stars in each row
        for k in range(1, i + 1):
            print("*", end=" ")

        # Move to next line after each row
        print()


# Get input from user
rows = int(input("Enter the number of rows for the pyramid: "))
print_star_pyramid(rows)
