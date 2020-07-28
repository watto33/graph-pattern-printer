# Function to display a pretty banner at the start.
def print_banner():
    print('\n\n')
    print('-'*100)
    print('\nWelcome to Graph generator\n')
    print('-'*100)
    print('\n\n')


# Function to print the string at the top of the max column.
def make_doll(colCount):
    print(' o ', end='\n')
    print(' ' * colCount, end="")
    print('/|\\', end='\n')
    print(' ' * colCount, end="")
    print('< >', end='')


print_banner()

# Get input from user.
str_input_series = input("Enter the input sequence to generate the graph\n")

# Convert user entered string to number.
str_input_series_arr = str_input_series.split()
num_input = []
for i in str_input_series_arr:
    num_input.append(int(i))

row_count = col_count = temp_count = max_column = 0

# To identify the number of rows and columns.

for i in range(len(num_input)):
    col_count += num_input[i]
    if i % 2 == 0:
        temp_count += num_input[i]
    else:
        temp_count -= num_input[i]
    if(temp_count > row_count):
        row_count = temp_count
        max_column = col_count

'''
Creating an empty 2D Array (Nested Lists) of size Row Count x Column Count.

The extra one added to row count is to print the extra string to be displayed at top of max column.
'''

matrix = [[0 for x in range(col_count)] for y in range(row_count+1)]

# Filling the array initially with spaces.

for i in range(row_count+1):
    for j in range(col_count):
        matrix[i][j] = ' '

row_ctr = col_ctr = 0

# Storing the symbols corresponding to rows and columns

for i in range(len(num_input)):
    for j in range(num_input[i]):
        if i % 2 == 1:
            row_ctr -= 1
            matrix[row_ctr][col_ctr] = '\\'
        else:
            matrix[row_ctr][col_ctr] = '/'
            row_ctr += 1
        col_ctr += 1


# Printing the matrix to display the graph
print('\n\nThe following graph is generated based on the user input\n\n')
for i in range(row_count, -1, -1):
    for j in range(col_count):
        if j == max_column-1 and i == row_count:
            make_doll(max_column-1)
        else:
            if j == max_column:
                print(' ', end='')
            print(matrix[i][j], end="")
    print('')
