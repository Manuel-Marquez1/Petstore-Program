#Our pet store will start vy greeting the customer.
#python files will end with .py
print("**************************")
print("******  WELCOME TO   ***********")
print("********    OUR     ********")
print("******** PET STORE   ******")
print("****************************")

num_dogs = 10
num_cats = 8
num_birds = 25

#Getting user data
print("Please enter your name: ")
name = input()
print("Please enter your last name")
last_name = input()


#concatenation
#It takes 2 strings and adds them together.
#We added a string to our full name using quotation marks.

full_name = name + " " + last_name
print("Thank you for your visit", full_name)

#Print how many dogs, cats and birds we have in the store-
print("The number of dogs in the store are: " , num_dogs)
print("The number of cats in the store are: " , num_cats)
print("The number of birds in the store are: ", num_birds)
#print the total

print("The total number of animals we have in the store are", num_dogs + num_cats + num_birds)


