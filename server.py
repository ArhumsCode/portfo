

import csv
from flask import Flask,render_template, request, redirect
app = Flask(__name__)
print(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    email = data['email']
    subject = data['subject']
    message = data['message']

    with open('database.txt', 'a') as database:
        database.write(f'Email: {email} \nSubject: {subject}\nMessage: {message}\n\n')

def write_to_csv(data):
    email = data['email']
    subject = data['subject']
    message = data['message']

    with open('database.csv', 'a') as database2:
        csv_writer = csv.writer(database2, delimiter=',' , quotechar='"' , quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return ' did not submit form properly'
    else:
        'something went wrong try again'