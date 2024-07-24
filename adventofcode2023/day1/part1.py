#Advent of Code 2023 - day1 
# The goal is to process the file input.txt to extract the first and last digit from each line, combining them to form a two-digit number.
# Calculating the sum of these numbers and then printing the result. 

with open('input.txt') as input:
    input_list= input.read().splitlines() #reads all the lines of the input and removes the newline symbol

sum = 0 #declaring the sum variable

for x in input_list:
    string = x.strip() #removes any leading/trailing whitespace from the string
    digit_list = [i for i in string if i.isdigit()] #creates a list with the digits 
    sum += int((digit_list[0]) + (digit_list[-1])) #converts the first and last digit in the list to a single integer and add to the sum
    

print(sum)
