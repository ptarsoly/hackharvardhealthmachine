########### Python 2.7 #############
import httplib, urllib, base64

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'ripperoni',
}

params = urllib.urlencode({
    # Request parameters
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'headPose,emotion',
})

try:
    conn = httplib.HTTPSConnection('eastus2.api.cognitive.microsoft.com')
    conn.request("POST", "/face/v1.0/detect?%s" % params, '{"url":"https://s3.amazonaws.com/derbyhacks/emily.jpg"}', headers) ##put url of target image here
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################


