import sys, urllib.parse,urllib.request

print('https://jsonplaceholder.typicode.com/post/1')
url = 'https://jsonplaceholder.typicode.com'
param='/posts/1'
try:
    print('Url:',url+param)
    response = urllib.request.urlopen(url+param)
    payload= response.read()
    print('Payload:',payload)
except:
    e = sys.exc_info()[0]
    print("error:%s"%e)
    

