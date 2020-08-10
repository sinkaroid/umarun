import base64
import zlib
import urllib.request
from colorama import Fore, Style


print(Fore.RED)
print("""                                      
 _   _ _ __ ___   __ _ _ __ _   _ _ __  
| | | | '_ ` _ \ / _` | '__| | | | '_ \ 
| |_| | | | | | | (_| | |  | |_| | | | |
 \__,_|_| |_| |_|\__,_|_|   \__,_|_| |_|                                                  
""")
print(Style.RESET_ALL)
print ("Umarun - unMarshal\n")
print ("1. find b64bytecode")
print ("2. redacted b64bytecode")
print ("3. gotta flag")
print (30 * '-')

choice = input('args [1-3] : ')
choice = int(choice)
 
### Take
if choice == 1:
        url = input('raw paste: ')
        file = urllib.request.urlopen(url) # nosec

        for line in file:
	        decoded_line = line.decode("utf-8")
	        print(decoded_line)
        rubbishword = decoded_line

        b64 = base64.b64decode(rubbishword)
        print(b64)

elif choice == 2:
        url = input('raw paste: ')
        file = urllib.request.urlopen(url) # nosec

        for line in file:
	        decoded_line = line.decode("utf-8")
	        print(decoded_line)
        rubbishword = decoded_line

        b64 = base64.b64decode(rubbishword)
        goblok = zlib.decompress(b64)
        print(goblok)

elif choice == 3:
        print('Pls use redacted instead')

else:    ## default ##
        print ("Invalid number")