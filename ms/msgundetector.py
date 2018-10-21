import http.client, urllib.request, urllib.parse, urllib.error, base64, json

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'try_again',
}

params = urllib.parse.urlencode({
    # Request parameters
    'visualFeatures': 'Categories,Tags,Description',
    'language': 'en',
})

try:
    conn = http.client.HTTPSConnection('eastus2.api.cognitive.microsoft.com')
    conn.request("POST", "/vision/v1.0/analyze?%s" % params, '{"url":"https://s3.amazonaws.com/securecampus/nerf1.jpeg"}', headers) ##put target image url here
    response = conn.getresponse()
    data = response.read()
    ## print(data)
    jsondata = json.loads(data)
    ##print(jsondata)
    ##print(jsondata['tags'][0]['name'])
    ##print(jsondata['description']['captions'][0]['text'])

    if jsondata['tags'][0]['name'] == 'gun' or 'gun' in jsondata['description']['captions'][0]['text']:
        print('gun')
    else:
        print('no')
    
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
