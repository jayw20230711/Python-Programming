"""
Python Requests post() Method

Definition and Usage
The post() method sends a POST request to the specified url.

The post() method is used when you want to send some data to the server.

Syntax
requests.post(url, data={key: value}, json={key: value}, args)

args means zero or more of the named arguments in the parameter table below. Example:

requests.post(url, data = myobj, timeout=2.50)

Parameter		    Description
url		            Required. The url of the request
data		        Optional. A dictionary, list of tuples, bytes or a file object to send to the specified url
json		        Optional. A JSON object to send to the specified url
files		        Optional. A dictionary of files to send to the specified url
allow_redirects		Optional. A Boolean to enable/disable redirection.
                    Default True (allowing redirects)
auth		        Optional. A tuple to enable a certain HTTP authentication.
                    Default None
cert		        Optional. A String or Tuple specifying a cert file or key.
                    Default None
cookies		        Optional. A dictionary of cookies to send to the specified url.
                    Default None
headers		        Optional. A dictionary of HTTP headers to send to the specified url.
                    Default None
proxies		        Optional. A dictionary of the protocol to the proxy url.
                    Default None
stream		        Optional. A Boolean indication if the response should be immediately downloaded (False) or streamed (True).
                    Default False
timeout		        Optional. A number, or a tuple, indicating how many seconds to wait for the client to make a connection and/or send a response.
                    Default None which means the request will continue until the connection is closed
verify	            Optional. A Boolean or a String indication to verify the servers TLS certificate or not.
                    Default True

Return Value
A requests.Response object.

"""
import requests

url = 'https://www.w3schools.com/python/demopage.php'

myobj = {'somekey': 'somevalue'}

x = requests.post(url, json=myobj)

print(x.text)
