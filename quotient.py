#entering numbers and getting a sum
xstring=input("Enter a number: ")
ystring=input("Enter a second number: ")
x=int(xstring)
y=int(ystring)

print("The quotient of ",x," and ",y," is ",x//y, "with a remainder of ", x%y)

def happyBirthday(name):
	bdaySong='''
	"Happy Birthday to you!
	Happy Birthday to you!
	Happy Birthday, dear",name,".
	Happy Birthday to you!"
	'''

	print(bdaySong)


happyBirthday(Emily)
