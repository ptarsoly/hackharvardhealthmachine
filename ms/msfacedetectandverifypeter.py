########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64, json, boto3, sys, os, time


faceUrl = sys.argv[1]

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'wrecked',
}

params = urllib.parse.urlencode({
    # Request parameters
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'headPose,emotion',
})

try:
    conn = http.client.HTTPSConnection('eastus2.api.cognitive.microsoft.com')
    urlParam = '{"url":"' + faceUrl +'"}'
    ##conn.request("POST", "/face/v1.0/detect?%s" % params, '{"url":"https://s3.amazonaws.com/shellhacks2018/peter.jpg"}', headers) ##put url of target image here
    conn.request("POST", "/face/v1.0/detect?%s" % params, urlParam, headers)
    response = conn.getresponse()
    str_response = response.read().decode('utf-8')
    jsondata = json.loads(str_response)
##    data = response.read()
##    ##print(data)
##    jsondata = json.loads(data)
    print(jsondata)
    print('the face id detected is ')
    print(jsondata[0]['faceId'])
    targetfaceid = jsondata[0]['faceId']
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
print('now verifying...')

flag = 0

params = urllib.parse.urlencode({
})

bodystring =     '{"faceId":"'+targetfaceid+'","personId":"294753e5-006c-43b1-8844-6eb8d7073de1","personGroupId":"fitxlab" }'

try:
    conn = http.client.HTTPSConnection('eastus2.api.cognitive.microsoft.com')
    conn.request("POST", "/face/v1.0/verify?%s" % params, bodystring, headers)
    response = conn.getresponse()
    str_response = response.read().decode('utf-8')
    jsondata = json.loads(str_response)
##    data = response.read()
##    ##print(data)
##    jsondata = json.loads(data)

    print(jsondata)
    print(jsondata['isIdentical'])
    print(jsondata['confidence'])

    if jsondata['isIdentical'] == True and jsondata['confidence'] > 0.7:
        print('Peter')
        print ('done')
        flag = 1
    else:
        print ('checking for woodle')
        
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))


if flag == 1:
    sys.exit()

params = urllib.parse.urlencode({
})

bodystring =     '{"faceId":"'+targetfaceid+'","personId":"294753e5-006c-43b1-8844-6eb8d7073de1","personGroupId":"fitxlab" }'

try:
    conn = http.client.HTTPSConnection('eastus2.api.cognitive.microsoft.com')
    conn.request("POST", "/face/v1.0/verify?%s" % params, bodystring, headers)
    response = conn.getresponse()
    str_response = response.read().decode('utf-8')
    jsondata = json.loads(str_response)
##    data = response.read()
##    ##print(data)
##    jsondata = json.loads(data)

    print(jsondata)
    print(jsondata['isIdentical'])
    print(jsondata['confidence'])

    if jsondata['isIdentical'] == True and jsondata['confidence'] > 0.7:
        print('Peter')
        print ('done')
        flag = 1
    else:
        print ('checking for woodle')
        
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))



