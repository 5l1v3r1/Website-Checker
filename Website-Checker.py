try:
	import requests
	pass
except ImportError as ierequests:
	print("Requests Module Is Missing From Your Machine")
	print("Run 'sudo pip3 install requests'")
	sys.exit()
try:
	import sys
	pass
except ImportError as iesys:
	print("Sys Module Is Missing From Your Machine")
	print("Run 'sudo pip3 install sys'")
	sys.exit()
try:
	import os
	pass
except ImportError as  ieos:
	print("Os Module Is Missing From Your Machine")
	print("Run 'sudo pip3 install os'")
	sys.exit()

os.system("clear")

print("""
				================================================================
				#			  Website Checker		       #
				################################################################
				+	         Check A Website If It Is Up Or Down	       +
				+		  Follow Me On github: hacker900123	       +
				+			       Enjoy!		               +
				################################################################
				================================================================
""")


url = input("Enter Website To Check: ")


try:
	response =requests.get(url)
	print("Checking " + url)
	check_resp = response.raise_for_status()

except Exception as E:
	print("Website Is Down And Not Available")

else:
	print("Website Is Up And Available")


