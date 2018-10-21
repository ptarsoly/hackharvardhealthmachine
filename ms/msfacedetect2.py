########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64, json

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'hahahahaha',
}

params = urllib.parse.urlencode({
    # Request parameters
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'headPose,emotion',
})

try:
    conn = http.client.HTTPSConnection('eastus2.api.cognitive.microsoft.com')
    conn.request("POST", "/face/v1.0/detect?%s" % params, '{"url":"https://s3.amazonaws.com/derbyhacks/emily.jpg"}', headers) ##put url of target image here
    response = conn.getresponse()
    str_response = response.read().decode('utf-8')
    jsondata = json.loads(str_response)
##    data = response.read()
##    ##print(data)
##    jsondata = json.loads(data)
    print(jsondata)
    print(jsondata[0]['faceId'])
    roll = jsondata[0]['faceAttributes']['headPose']['roll']
    pitch = jsondata[0]['faceAttributes']['headPose']['pitch']
    yaw = jsondata[0]['faceAttributes']['headPose']['yaw']
    print (str(roll) + " " + str(pitch) + " " + str(yaw))
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
