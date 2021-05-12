# first create a version env, venv using py -3 -m venv venv or make the webserver2 the venv using
# py -3 -m venv web_server2
# next activate the venv using venv\Scripts\activate or web_server2\Scripts\activate
# do a pip install flask to install flask in this venv(webserver2)
# set FLASK_APP=server2.py....
# flask run
# this brings the url/addrss of my laptop
# turn on debug mode by set FLASK_ENV=development
# store css,js,asset files in static folder
# store html files in templates
# update locations, save, refresh
from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


# @app.route('/components.html')
# def components():
#     return render_template('components.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


# this is never called on the front end
# search for send message on index.html, go to form above ....form action="name of new route created(submit_form)"
# method "post/get"
# put name tags in the email, subject and message sections in the html files to enable u grab the data at the backend
# save info to a write_to_csv function
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('thankyou.html')
    else:
        return 'something went wrong'


def write_to_csv(data):
    with open('mydatabase.csv', mode='a', newline='') as mydatabase:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(mydatabase, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
