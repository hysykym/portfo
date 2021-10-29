from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/<string:page_name>')
def my_home(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject}, {message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            # data = request.form['email']
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something is wrong'


# @app.route('/blog/<username>')
# def blog(username=None):
#     return f'These are my thoughs of blog {username}'