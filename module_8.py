# Module 8: Input, Output & File Handling

# Reading from files — open() , read() , readline() , readlines()

# Open a file for reading
file = open('data_types.py', 'r')

# Read the entire file
#content = file.read()
#print(content)
#file.close()

# Read the file line by line
#line = file.readline()
#print(line)

# Read lines into a list
lines = file.readlines()
#print(lines)
file.close()


# Writing to files — write mode ( w ) and append mode ( a )
# Write mode ( w )
# a append mode

# Open a file for writing in write mode
# file = open('data.txt', 'w')

# # Write to the file
# file.write('Hello, World!')
# file.write('\n')
# file.write('Hello, World!')
# file.write('\n')
# file.write('Hello, World!')
# file.close()


# Append to the file
file = open('data.txt', 'a')

# Append to the file
file.write('Atanu = atanu@gmail.com')
file.write('\n')
file.write('Sahinoor = sahinoor@gmail.com')
file.write('\n')
file.write('Rajesh = rajesh@gmail.com')

file.close()

# with statement for file handling

with open('data.txt', 'r') as file:
    content = file.read()
    print(content)


