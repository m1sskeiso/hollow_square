# Input the side length of the square
n = int(input("Enter the side length of the square: "))

# Loop to create the hollow square
for i in range(n):
    for j in range(n):
        # Print 'x' for the border and space for the hollow part
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print('x', end='')
        else:
            print(' ', end='')
    print()  # Move to the next line after finishing a row
