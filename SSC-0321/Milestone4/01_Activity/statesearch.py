# Pablo Sanchez
# Python version 2.7.16
# Dictionary Searches
#
# State Capitol Search

# Allow for 5 Searches
# Save Results of search to state_result.txt

#########################################
# IMPORT THE STATES & CAPITOLS
#########################################

# 2. Explain why we start with an empty Dictionary
# A: We start with an empty dictionary as a placeholder. Usually used if we want a user to populate it using input function or if we will be later
# populate it with a read function that reads an external file.

# Create Blank Dictionary
states = {}

# 3. Explain how the FOR Loop here is used to import the data
#  and separate it into KEY / VALUE pairs.
# A: The FOR loop is reading each line on the text file and split it using the "," delimeter. The value to the left is the key and to
# the right becomes the value within the dictionaty which is stored in the "states" list.
count = 5

# Import State & Capitol in the blank Dictionary
f = open('states.txt', 'r')

for line in f:
    (key, val) = line.split(',')
    states[key] = val

f.close()

# User must enter the name of the state to search
print ('STATE SEARCH SCRIPT')
print ('Please enter the name of 5 states to search for.')

# 4. Create a variable called count with an assigned value of 5


##########################################
# LOOP THE SEARCH & WRITE TO EXTERNAL FILE
##########################################

# Open Report file
f= open('state_results.txt', 'w+')

# 5. Describe how the WHILE Loop uses the count variable as a control.
# A:
# 6. How is the count variable updated?
# A:
# 7. What is the effect?
# A:
# 8. Explain how states[search] returns a value.
# A:

# Use a Loop to run search 5 times
while count > 0:
    search = str(raw_input('Enter Name of State: ').title())

    # Check the Dictionary for the State / Capitol result
    if search in states:
        print ('The Capitol of ' + search + ' is ' + states[search])
        count -= 1
        print ('Remaining number of searches: ' + str(count))
        f.write('State: ' + search + ' Capitol: ' + states[search])
    else:
        print ("You have entered an incorrect value.")

f.close()
###########################################

# 9. Rewrite the LOOP SEARCH Section above (Lines 22 - 28) to utilize with open()

# 10. Test and confirm your script works before submitting to FSO!