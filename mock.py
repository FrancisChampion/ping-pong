import random

# Create an empty array
array = []

# Iterate 100 times
for i in range(100):

    # Generate a random float value between 50 and 150
    value = random.randint(50, 150)

    # Append the value to the array
    array.append(value)

# Print the array
print(array)  
count = 0

# Iterate over the array
for value in array:

    # Check if the value is smaller than 100
    if value < 100:

        # Increment the count
        count += 1

# Print the count
print(count) 
# this is the end of the code