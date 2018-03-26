import urllib.request as urllib

serverURL = "http://localhost:5000/"

stateURL = serverURL + "wait"

content = urllib.urlopen(stateURL).read()
print(content)