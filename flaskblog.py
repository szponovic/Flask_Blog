from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Tomasz Biskupski',
        'title': 'Blog Post One',
        'content': 'First post content',
        'date_posted': '01 october 2019'
    },
{
        'author': 'Lord Szponovic',
        'title': 'Blog Post Two',
        'content': 'Second post content',
        'date_posted': '02 october 2019'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)