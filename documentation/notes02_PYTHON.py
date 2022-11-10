'''
PYTHON NOTES

This serves as my annotations on the Python Documentation
LINK: 

'''

'''
Chapter 2: Python Interpreter
'''
# Quickstart Guide:
'''
Running the Interpreter in BASH: python3
Exiting the Interpreter in BASH: Ctrl+D or quit()
'''

# 2.1.1: Argument Passing
'''
- When running in the Interpreter...
	- script name and addt'l arguments are turned into a list of strings and assigned to
		argv (contained in the sys module)
		- accessed using 'from import argv'
		
- argv
	- When argv is empty, argv[0] = ''
	- When the script name is given as '-' (standard), argv[0] = '-'
	- When the -c command is used, argv[0] = '-c'
	- When the -m module is used, argv[0] is set to the full name of the located module
'''

# 3.2-4: Syntax

# LOOPS:
'''
while loops:

while CONDITIONAL:
	# code
# exited by deleting the tab


for loops:
	- select variable to iterate and the dataset to iterate over
	
EX: words = ['cat', 'dog', 'window']
for w in words:
	print(w, len(w))

*this will print each word in the list and the length of each string*
'''