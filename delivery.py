#! /usr/bin/env python3
print('Content-type: text/html\n')
import cgi

form = cgi.FieldStorage()

html = """
<!doctype html>
<html>
<head><meta charset="utf-8">
<title>Robot Delivery System Confirmation</title></head>
    <body>
    <h1>Robot Delivery System Confirmation</h1>
    <p>You have selected to have a {delivery} delivered by {delivery_method}.</p>
<p>Your total comes to $ {cost}.</p>
    </body>
</html>"""

delivery = form.getfirst("delivery")
delivery_method = form.getfirst("delivery_method")
cost = form.getfirst("cost")


if delivery_method == "drone":
	cost.append(10)
elif delivery_method == "self driving car":
	cost.append(20)
elif delivery_method == "giant robot":
	cost.append(1000)
		
print(html.format(delivery = delivery, delivery_method = delivery_method, cost = cost))
	