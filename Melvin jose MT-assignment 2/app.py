from flask import Flask, render_template, url_for 

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')



@app.route("/blog")
def blog():
    return render_template('blog.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/signin")
def signin():
    return render_template('signin.html')

@app.route("/signup")
def signup():
    return render_template('signup.html')        

#@app.route("/profiles/<username>")
#def profiles(username):
 #   return "hello" + username 
   
#@app.route('/blog/<post_id>')
#def show_post(post_id):
 #   return post_id
     