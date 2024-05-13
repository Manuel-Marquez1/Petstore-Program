print("Welcome, this program will convert miles to KM")

print("Enter the number of miles: ")
miles = input() #string

#Input always returns a string.
#That is why we need to convert our data types.

miles = float(miles)

# 1 mile = 1.609 kms
kilometers = miles * 1.609

print("Number of miles you entered:" , miles)
print("Answer in KM: ", kilometers)
