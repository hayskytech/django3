from django.http import HttpResponse
from django.shortcuts import render
import sqlite3

def home(r):
	# return HttpResponse("Hello world")
	return render(r, "home.html")

def about(req):
	return render(req, "about.html")

def contact(req):
	return render(req, "contact.html")

def books(req):
	con = sqlite3.connect("db.sqlite3")
	cur = con.cursor()
	res = cur.execute("SELECT name from sqlite_master")
	tables = res.fetchall()
	if ('books',) not in tables:
		cur.execute("""CREATE TABLE books
									(id INTEGER NOT NULL,
									book TEXT NOT NULL,
									year INT NULL,
									price INT NULL,
									PRIMARY KEY("id" AUTOINCREMENT)
									);""")

	if req.POST.get("add_book"):

		book = req.POST.get("book")
		year = req.POST.get("year")
		price = req.POST.get("price")
		data = (book, year, price)
		cur.execute("INSERT INTO books (book,year,price) VALUES (?,?,?)", data)
		con.commit()

	if req.POST.get("delete"):
		id = req.POST.get("id")
		cur.execute("DELETE FROM books WHERE id = ?" , id)
		con.commit()

	books = cur.execute("SELECT * FROM books").fetchall()
	
	x = {
		"books" : books
	}

	


	return render(req, "books.html", x )


def book_edit(req):
	con = sqlite3.connect("db.sqlite3")
	cur = con.cursor()
	id = req.POST.get("id")
	msg = ""
	if req.POST.get("save"):
		book = req.POST.get("book")
		year = req.POST.get("year")
		price = req.POST.get("price")

		cur.execute("UPDATE books set book=?, year=?, price=?  WHERE id=?", (book, year, price ,id) )
		con.commit()
		msg = "Book updated."

	data = cur.execute("SELECT * FROM books WHERE id=?" , id ).fetchone()
	x = {
		"id" : id,
		"book" : data[1],
		"year" : data[2],
		"price" : data[3],
		"msg" : msg
	}

	return render(req, "book_edit.html", x )