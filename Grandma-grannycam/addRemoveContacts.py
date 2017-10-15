#!/usr/bin/python3
import cgitb
cgitb.enable()
import cgi
from carefullyLoadYaml import *
import smtplib
import sys

clientName= cgi.escape(cgi.form.getvalue("client"))

fingerFile = "fingersToNames.yml"
#fingerToName = carefullyLoadYaml(fingerFile)

nameFile = "namesToContacts.yml"
#nameToContact = carefullyLoadYaml(nameFile)

carrierFile = "emailTextCodes.yml"
#carrierDB = carefullyLoadYaml(carrierFile)

def genCarrierPulldown(n):
    carrierDB = carefullyLoadYaml(carrierFile)
    s='<select name="carrier%d">' % (n,)+"\n"
    for carrier in carrierDB.keys():
        s+= '<option value="%s">%s</option>' % (carrier, carrier)+"\n"
    s+='</select>'
    s+="\n"
    return s
def genFingerPulldown(n):
    return """
<select name="finger%d">
<option value="index">Index</option>
<option value="middle">Middle</option>
<option value="ring">Ring</option>
<option value="pinky">Pinky</option>
</select>
""" % (n,)

def genAddTableRows(nn):
    s=""
    for n in range(nn):
        s+="""
 <tr>
    <td><input type="text" name="firstname%d" size="20"></td>
    <td><input type="text" name="lastname%d" size="20"></td>
    <td> %s </td>
    <td><input type="tel" name="phone%d" size="12"></td>
    <td> %s </td>
  </tr>
  """ % (n, n, genCarrierPulldown(n), n, genFingerPulldown(n))
    return s
    
def genMainPage():
    print(  """
<!DOCTYPE html>
<html>
<head>
<style>
table {
    font-family: arial, sans-serif;
    border-collapse: collapse;
    width: 100%%  ;
}

td, th {
    border: 1px solid #dddddd;
    text-align: left;
    padding: 8px;
}

tr:nth-child(even) {
    background-color: #dddddd;
}
</style>
</head>
<body>
<strong>
Editing Contacts for client: %s
</strong>
<table>
  <tr>
    <th>First Name</th>
    <th>Last Name</th>
    <th>Carrier</th>
    <th>Phone #</th>
    <th>finger</th>
  </tr>
 %s
</table>
<form action="submitContactEdits.py">
<input type="submit" value="submit changes"
<input type="hidden" value="%s">
</form>
</body>
</html>
"""  % (clientName, genAddTableRows(4), clientName) )

if __name__ == "__main__":
    # execute only if run as a script
    genMainPage()
