from flask import Flask, render_template

app = Flask(__name__)


@app.route('/profile/<uname>')
def index(uname):
    return render_template('index.html', usrName=uname, active=True)


@app.route('/book')
def book():
    books = ['book1', 'book4', 'book2', 'book3']
    return render_template('book1.html', books=books)


@app.route('/book2')
def objects():
    books1 = ['book1', 'book4', 'book2', 'book3']
    books = [{'name': 'book', 'author': 'author1','cover':"http://www.publishwithprasen.com/wp-content/uploads/2014/05/fruits-ebook-cover-Full-name-Georgia-9-Oct-2013.jpg"},
             {'name': 'book1', 'author': 'author2','cover':"http://www.publishwithprasen.com/wp-content/uploads/2014/05/fruits-ebook-cover-Full-name-Georgia-9-Oct-2013.jpg"},
             {'name': 'book2', 'author': 'author3','cover':"http://www.publishwithprasen.com/wp-content/uploads/2014/05/fruits-ebook-cover-Full-name-Georgia-9-Oct-2013.jpg"}]
    return render_template('book.html', books=books,books1=books1)


app.run(debug=True)
