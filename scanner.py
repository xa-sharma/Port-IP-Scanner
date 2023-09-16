import sys
import socket
from datetime import datetime

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #It will Translate hostname to IPv4
else:
	print("Invalid amount of arguments.") #There are two arguments and if one missed it will print this, 1st arguement is python3 "scanner.py" and 2nd one is "<ip>"
	print("Syntax: python3 scanner.py") 


print("-" * 50)                                  #This is to make a pretty banner on the top, You can avoid this if don't want to use ... (Line no. - 12, 13, 14, 15)
print("Scanning target "+target)
print("Time started: "+str(datetime.now()))
print("-" * 50)

try:
	for port in range(50,85):                      #Generally we scan port 50 to 85 to get DNS and http
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port)) #returns an error indicator - if port is open it throws a 0, otherwise 1
		if result == 0:
			print("Port {} is open".format(port))
		s.close()

except KeyboardInterrupt:                      #these 3 except statements are used to take a look at errors, You guys can also avoid it ... but i recommend using these expect statements for clearity and errors
	print("\nExiting program.")
	sys.exit()
	
except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()

except socket.error:
	print("Could not connect to server.")
	sys.exit()
