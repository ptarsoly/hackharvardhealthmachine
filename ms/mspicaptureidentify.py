import requests, json, sys, os

param = sys.argv[1]

commandstring = "sudo raspistill -w 800 -h 600 -rot 90 -o candidate" + param + ".jpg"

os.system(commandstring)

commandstring = "sudo python uploadjpegtos3bucket.py candidate" + param + ".jpg candidate" + param + ".jpg"

os.system(commandstring)

url = "https://eastus.api.cognitive.microsoft.com/face/v1.0/detect"

querystring = {"returnFaceId":"true","returnFaceLandmarks":"false"}

payload = "{\r\n    \"url\": \"https://s3.amazonaws.com/hackharvard/candidate" + param + ".jpg\"\r\n}"
headers = {
    'Ocp-Apim-subscription-Key': "sorry_not_here",
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "f6d417e5-50dc-4268-b1e4-9a671fa78cf5"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

##print(response.text)

json_data = json.loads(response.text)

print (json_data[0]["faceId"])

fID1 =  json_data[0]["faceId"]

querystring = {"returnFaceId":"true","returnFaceLandmarks":"false"}

payload = "{\r\n    \"url\": \"https://s3.amazonaws.com/shellhacks2018/peter.jpg\"\r\n}"
headers = {
    'Ocp-Apim-subscription-Key': "fe27f8222d5f4be0964ec044488b3941",
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "f6d417e5-50dc-4268-b1e4-9a671fa78cf5"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

##print(response.text)

json_data = json.loads(response.text)

print (json_data[0]["faceId"])

fID2 =  json_data[0]["faceId"]


url2 = "https://eastus.api.cognitive.microsoft.com/face/v1.0/verify"

payload = '{\r\n   "faceId1": "' + fID1 +'",\r\n    \"faceId2\": "' + fID2 + '"\r\n}'

print (payload)

headers = {
    'Content-Type': "application/json",
    'Ocp-Apim-Subscription-Key': "fe27f8222d5f4be0964ec044488b3941",
    'cache-control': "no-cache",
    'Postman-Token': "4f98f68d-dc71-4bf7-b56f-cd579d976da9"
    }

response = requests.request("POST", url2, data=payload, headers=headers)

print(response.text)

json_data = json.loads(response.text)

if json_data["isIdentical"] == True:
    print ("Peter")
    sys.exit()



querystring = {"returnFaceId":"true","returnFaceLandmarks":"false"}

payload = "{\r\n    \"url\": \"https://s3.amazonaws.com/shellhacks2018/chris.jpg\"\r\n}"
headers = {
    'Ocp-Apim-subscription-Key': "fe27f8222d5f4be0964ec044488b3941",
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "f6d417e5-50dc-4268-b1e4-9a671fa78cf5"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

##print(response.text)

json_data = json.loads(response.text)

print (json_data[0]["faceId"])

fID2 =  json_data[0]["faceId"]


url2 = "https://eastus.api.cognitive.microsoft.com/face/v1.0/verify"

payload = '{\r\n   "faceId1": "' + fID1 +'",\r\n    \"faceId2\": "' + fID2 + '"\r\n}'

print (payload)

headers = {
    'Content-Type': "application/json",
    'Ocp-Apim-Subscription-Key': "fe27f8222d5f4be0964ec044488b3941",
    'cache-control': "no-cache",
    'Postman-Token': "4f98f68d-dc71-4bf7-b56f-cd579d976da9"
    }

response = requests.request("POST", url2, data=payload, headers=headers)

print(response.text)

json_data = json.loads(response.text)

if json_data["isIdentical"] == True:
    print ("Woodle")
    sys.exit()

print ("unidentified")
















