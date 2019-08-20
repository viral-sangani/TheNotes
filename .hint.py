import os, sys

# print ( sys.argv[1])
if len(sys.argv) == 3: 
	if sys.argv[2] == '-l':
		if "md" not in sys.argv[1]:
			os.system("less ~/TheNotes/"+ sys.argv[1] + ".md")
		else:
			os.system("less ~/TheNotes/"+ sys.argv[1])

else:
	if "md" not in sys.argv[1]:
		os.system("mdless ~/TheNotes/"+ sys.argv[1] + ".md")
	else:
		os.system("mdless ~/TheNotes/"+ sys.argv[1])