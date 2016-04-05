# import statements
import copytext
from flask import Flask, render_template, url_for
import sys
import urllib2

# give us the settings and methods to freeze this app
import settings

# init flask
app = Flask(__name__, static_folder=settings.static_files_location,
            template_folder=settings.template_folders_location)
# datawork
dorms = {}
dormlist = {}

copy = copytext.Copy('dataset.xlsx')

# routing
@app.route('/dorms/andrews')
@app.route('/dorms/blanton')
@app.route('/dorms/brackenridge')
def dorm_display():
    context = dorms
    #candidateId = (context['candidate_name'] + context['major'] + context['year']).replace(" ", "_").replace("/", "_")
   #categoryId = context['position'].replace(" ","_")
    return render_template('dorm.html', **context)


@app.route('/')
def main_display():
    return render_template('main.html')

if __name__ == '__main__': app.run(debug=True)
