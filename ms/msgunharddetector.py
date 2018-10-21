import http.client, urllib.request, urllib.parse, urllib.error, base64, json, os, boto3, time


##filename = 'testgun.jpg'
##com = 'sudo fswebcam -q ' + filename
##
##print (com)
##
##
##
##time.sleep(1)
##os.system(com)
##time.sleep(2)
##
##sourceFile=filename
##s3 = boto3.resource('s3')
##
##bucket='securecampus'
##
##data = open(sourceFile, 'rb')
##s3.Bucket('securecampus').put_object(ACL='public-read', Key=sourceFile, Body=data)




headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'nice_try',
}

params = urllib.parse.urlencode({
    # Request parameters
    'visualFeatures': 'Categories,Tags,Description',
    'language': 'en',
})

try:
    conn = http.client.HTTPSConnection('eastus2.api.cognitive.microsoft.com')
    conn.request("POST", "/vision/v1.0/analyze?%s" % params, '{"url":"https://s3.amazonaws.com/securecampus/shooter3cctv.jpg"}', headers) ##put target image url here
    response = conn.getresponse()
    str_response = response.read().decode('utf-8')
    jsondata = json.loads(str_response)
##    data = response.read()
##    ## print(data)
##    jsondata = json.loads(data)
    print(jsondata)
    ##print(jsondata['tags'][0]['name'])
    ##print(jsondata['description']['captions'][0]['text'])

    

    if jsondata['tags'][0]['name'] == 'gun' or 'gun' in jsondata['description']['captions'][0]['text']:
        print('gun')
        ##os.system('sudo python3 leogun.py')
        connz = http.client.HTTPConnection("ec2-18-220-29-245,us-east-2,compute,amazonaws,com")

        payloadz = "{\n\t\"date\": \"2/18/2018\",\n\t\"door\": \"south entrance\",\n\t\"text\": \"possible gunman or banana man in building\",\n\t\"photoURL\": \"https://s3.amazonaws.com/securecampus/banana1.jpg\",\n\t\"coords\": [-80.422706, 37.233076]\n\t\n}"

        headersz = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "9d81c571-0834-43d1-8bd1-afc2f15113d1"
            }

        connz.request("POST", "data", payloadz, headersz)

        resz = connz.getresponse()
        dataz = resz.read()

        print(dataz.decode("utf-8"))
    else:
        print('no gun')

    if jsondata['tags'][0]['name'] == 'banana' or 'banana' in jsondata['description']['captions'][0]['text'] or 'banana' in jsondata['description']['tags'] :
        print('banana')
        os.system('sudo python3 leobanana.py')
    else:
        print('no banana')
    
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
