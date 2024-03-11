import utilities
import logging

logging.basicConfig(level=logging.DEBUG)

http = utilities.nac_http_RequestSession()

#result = http.get("https://www.google.com")
result = http.get("http://httpbin.org/ip")

print("Google response", result)
