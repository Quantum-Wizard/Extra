# Reading already made list of contact and sending message
import pandas as pd
import pywhatkit
# Enter the location of Contact.xlsx
excel_data = pd.read_excel('Contact.xlsx')
data = pd.DataFrame(excel_data, columns=['Name', 'Contact Number'])
input_name = input("Enter person's name:")
abc = ""
for i in range(0, len(data['Name'])):
    if data['Name'][i].lower() == input_name.lower():
        abc = data['Name'][i]+" has the number "+str(data['Contact Number'][i])
        value = str(data['Contact Number'][i])
	# Here +yy is the dialing code of the country and HH, MM is the time you want to send the message.
        pywhatkit.sendwhatmsg("+yy"+value, "Enter Your Message Here", HH, MM)
        break
else:
    print ("\nNo matching name was found.")
print("\n"+abc)
