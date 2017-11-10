from flask import Flask, render_template, request
import urllib2, json

my_app = Flask(__name__)

@my_app.route('/')
def root():
    u = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=k0yAWq3j6aknMRkn1bHKTeLYeLuTV0uk5HBWfeKW")
    info = u.read()
    d = json.loads(info)
    img = d['hdurl']
    explanation = d['explanation']
    return render_template("root.html", img = img, explanation = explanation)

if __name__ == "__main__":
    my_app.debug = True
    my_app.run()

