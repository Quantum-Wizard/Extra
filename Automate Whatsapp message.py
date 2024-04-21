# Creating list of contact and sending message
import re
import pywhatkit
name = ["Hamelton", "Brian"]
# Here +yy is the dialing code of the country and xxxxxxxxxx is the phone number.
contact_number = ["+yyxxxxxxxxxx", "+yyxxxxxxxxxx"]
input_name = input("Enter person's name:")
abc = ""
for i in range(0, len(name)):
    if name[i].lower() == input_name.lower():
        abc = name[i]+" has the number "+contact_number[i]
        value = contact_number[i]
	    # HH, MM is the time you want to send the message.
        pywhatkit.sendwhatmsg(value, "Enter Your Message Here", HH, MM)
        break
else:
    print ("\nNo matching name was found.")
print("\n"+abc)
