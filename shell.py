from datetime import datetime
from sys import platform as flat

# datetime object containing current date and time
now = datetime.now()

# dd/mm/YY H:M:S
l1 =  "Python 3.8.10 (default, " + now.strftime("%d/%m/%Y %H:%M:%S") + ")"
l2 = "(Python Shell 3.8.1) on " + flat
print("Python 3.8.10 ", l1)
print(l2)
print("Type 'help', 'copyright', 'credits' or 'license' for more information.")
while True:
	x = input(">>> ")
	if x == 'exit':
		break

	try:
		y = eval(x)
		if y: print(y)
	except:
		try:
			exec(x)
		except Exception as e:
			print("error:", e)
