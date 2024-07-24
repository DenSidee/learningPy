#Advent of Code 2023 - day1.part2
# The goal is to process the file input.txt to extract the first and last number from each line, wether a digit or a spelled word, combining them to form a two-digit number.
# Calculating the sum of these numbers and then printing the result. 


with open('input.txt') as input:
    input_list = input.read().splitlines()

sum_digits = 0


num_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

for string in input_list: 

    digit_list = []  

    
    for i, char in enumerate(string): # goes through each character in the string | i-> [i] index of the character, char-> char
        

        for val, num in enumerate(num_list): 

            if num in string[i:i+len(num)]: #if the current spelled number is found starting at index i, adds it to digit list
                digit_list.append(str(val))  # If a number word is found, add its corresponding digit to digit_list.

        if char.isdigit(): 
            digit_list.append(char)  

    if digit_list:   
        sum_digits += int(digit_list[0] + digit_list[-1])


print(sum_digits)
