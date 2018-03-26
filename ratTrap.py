# install FLASK if not installed
# $pip install Flask

# to run
# FLASK_APP=receiver.py flask run

import urllib.request as urllib

serverURL = "http://localhost:5000/"

stateURL = serverURL + "wait"

content = urllib.urlopen(stateURL).read()
print(content)