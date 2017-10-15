
#!/usr/bin/python3
from carefullyLoadYaml import *
import smtplib
import sys

fingerFile = "fingersToNames.yml"
#fingerToName = carefullyLoadYaml(fingerFile)

nameFile = "namesToContacts.yml"
#nameToContact = carefullyLoadYaml(nameFile)

carrierFile = "emailTextCodes.yml"
#carrierDB = carefullyLoadYaml(carrierFile)

def genListClients():
    nameToContact = carefullyLoadYaml(nameFile)
    q = ""
    q += '<select name="client">'
    for name in nameToContact.keys():
        q += '<option value="%s">%s</option>' % (name, name) + "\n"
    q+='</select>'
    return q
def genMainPage():
    print(  """
<!DOCTYPE html>
<html><body>
<form action="addRemoveContacts.py">
<table>
<tr>
<td>
Client:
%s
</td>
<td>
Options:
</td>
<td>

<input type="submit" value="Edit Contacts">
</form>
<form action="enroll.py">
<input type="submit" value="Enroll Fingers">
</form>
</td>
</tr>
</table>
</body></html>

"""  % (genListClients(),) )

if __name__ == "__main__":
    # execute only if run as a script
    genMainPage()

