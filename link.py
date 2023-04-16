#!/usr/bin/env python

import cgi


# Send the response to the website
print("Content-type: text/html")
print()
print(f"""
<!DOCTYPE html>
<html>
<head>
    <title>My App</title>
</head>
<body>
    import GPS_fin
    <p>{from GPS_fin import *}</p>
</body>
</html>
""")
