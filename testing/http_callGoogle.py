import utilities

http = utilities.nac_http_RequestSession()

result = http.get("https://www.google.com")

print("Google response", result)
