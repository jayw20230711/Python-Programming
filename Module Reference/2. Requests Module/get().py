"""
Python Requests get() Method

Definition and Usage
The get() method sends a GET request to the specified url.

Syntax
requests.get(url, params={key: value}, args)

args means zero or more of the named arguments in the parameter table below. Example:

requests.get(url, timeout=2.50)

Parameter		    Description
url		            Required. The url of the request
params		        Optional. A dictionary, list of tuples or bytes to send as a query string.
                    Default None
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
verify              Optional. A Boolean or a String indication to verify the servers TLS certificate or not.
                    Default True

Return Value
The get() method returns a requests.Response object.

"""
import requests

x = requests.get('https://w3schools.com')

# Make a request to a web page, and return the status code:
print(x.status_code)
