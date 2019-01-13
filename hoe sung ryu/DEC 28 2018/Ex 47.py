
import requests
import pandas as pd
# Make a get request to get the latest position of the international space station from the opennotify api.
response = requests.get("http://api.open-notify.org/astros.json")

# Get the response data as a python object.  Verify that it's a dictionary.
info= response.json()

#using pandas!!!
people=info['people']
print(people)
df=pd.DataFrame(people)
print(f"There are {info['number']} people in the space right now ")
print(df.reindex(index=None,columns=['name','craft'])) #convert oder of columns and index







