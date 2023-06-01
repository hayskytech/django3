

from django.shortcuts import render

def main(req):
	return render(req, "about.html")
def contact(req):
	return render(req, "contact.html")