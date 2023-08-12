"""
Python Requests head() Method

Definition and Usage
The head() method sends a HEAD request to the specified url.

HEAD requests are done when you do not need the content of the file, but only the status_code or HTTP headers.

Syntax
requests.head(url, args)
args means zero or more of the named arguments in the parameter table below. Example:

requests.head(url, timeout=2.50)

Parameter		    Description
url		            Required. The url of the request
allow_redirects     Optional. A Boolean to enable/disable redirection.
                    Default False (not allowing redirects)
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
verify		        Optional. A Boolean or a String indication to verify the servers TLS certificate or not.
                    Default True

Return Value
The head() method returns a requests.Response object.

"""
import requests

# Make a HEAD request to a web page, and return the HTTP headers:
x = requests.head('https://www.w3schools.com/python/demopage.php')

print(x.headers)
