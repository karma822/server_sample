
# importing the requests library 
import requests 
import sys

# api-endpoint 
URL = "http://127.0.0.1:5000/"
print("enter uri for test: ")
URL = input()
uploaduri = URL + "upload"
downloaduri = URL + "download"

while True:
    print("enter command:")
    print("\tu: upload")
    print("\td: download")
    print("\tq: quit")
    command = input()
    if command == 'q':
        break
    
    elif command == 'u':
        #filename = secure_filename(file.filename)
        files = {'file': open('/home/sunny/Pictures/amazon_go_tech.png', 'rb')}
        #print(files.file)
        #request.files = ['/home/sunny/Pictures/amazon_go_tech.png']
        r = requests.post(url = uploaduri, files = files)
        print(r)
    
    elif command == 'd':
        # sending get request and saving the response as response object 
        r = requests.get(url = downloaduri, allow_redirects=True) 
    
        print(r)
        open('/home/sunny/project/server/client/return.jpg', 'wb').write(r.content)
    else :
        print("wrong command")