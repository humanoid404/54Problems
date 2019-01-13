import requests
import json


# Replace with the correct URL
url = "http://api_url"

myResponse = requests.get(url,auth=HTTPDigestAuth(raw_input("username: "), raw_input("Password: ")), verify=True)


if(myResponse.ok):
    jData = json.loads(myResponse.content)

    print("The response contains {0} properties".format(len(jData)))
    print("\n")
    for key in jData:
        print(key + " : " + jData[key])
else:
    myResponse.raise_for_status()