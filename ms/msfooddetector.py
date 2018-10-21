import requests
# If you are using a Jupyter notebook, uncomment the following line.
#%matplotlib inline
##import matplotlib.pyplot as plt
import json
##from PIL import Image
from io import BytesIO
import sys

# Replace <Subscription Key> with your valid subscription key.
subscription_key = "not_here"
assert subscription_key

# You must use the same region in your REST call as you used to get your
# subscription keys. For example, if you got your subscription keys from
# westus, replace "westcentralus" in the URI below with "westus".
#
# Free trial subscription keys are generated in the westcentralus region.
# If you use a free trial subscription key, you shouldn't need to change
# this region.
vision_base_url = "https://westus.api.cognitive.microsoft.com/vision/v2.0/"

analyze_url = vision_base_url + "analyze"

# Set image_url to the URL of an image that you want to analyze.
##image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Broadway_and_Times_Square_by_night.jpg/450px-Broadway_and_Times_Square_by_night.jpg"

##image_url = "https://thumbs.dreamstime.com/z/cheese-pizza-slice-11122880.jpg"
image_url = sys.argv[1]


headers = {'Ocp-Apim-Subscription-Key': subscription_key }
params  = {'visualFeatures': 'Categories,Description,Color'}
data    = {'url': image_url}
response = requests.post(analyze_url, headers=headers, params=params, json=data)
response.raise_for_status()

# The 'analysis' object contains various fields that describe the image. The most
# relevant caption for the image is obtained from the 'description' property.
analysis = response.json()
##print(json.dumps(response.json()))

out = json.dumps(response.json())

##print (analysis["description"])

for t in analysis['description']['tags'] :
    if t == 'food':
        print ("food found")
        sys.exit()
print ("no")


