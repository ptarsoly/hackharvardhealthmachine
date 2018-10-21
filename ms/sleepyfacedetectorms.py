########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64, json, os, sys, time, boto3

filename = 'sleepcheck.jpg'
com = 'sudo fswebcam -q ' + filename

print (com)

time.sleep(2)
os.system(com)
time.sleep(2)

sourceFile=filename
s3 = boto3.resource('s3')

bucket='lastaccesshero'

data = open(sourceFile, 'rb')
s3.Bucket('lastaccesshero').put_object(ACL='public-read', Key=sourceFile, Body=data)

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'not_so_fast',
}

params = urllib.parse.urlencode({
    # Request parameters
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'headPose,emotion',
})

try:
    conn = http.client.HTTPSConnection('eastus2.api.cognitive.microsoft.com')
    conn.request("POST", "/face/v1.0/detect?%s" % params, '{"url":"https://s3.amazonaws.com/lastaccesshero/sleepcheck.jpg"}', headers) ##put url of target image here
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

    alert = 0
    if roll > 2.0 or roll < -2.0:
        alert = 1
    if pitch > 2.0 or pitch < -2.0:
        alert = 1
    if yaw > 3.0 or yaw < -3.0:
        alert = 1

    if alert ==1:
        print('sleepyhed detected!!')
        ##do something to wake up the driver here
    else:
        print('good job, stay alert')
    
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
