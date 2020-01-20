from flask import Flask, render_template, redirect, request, send_file, url_for
import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/<string:page_name>')
def page_load(page_name):
    return render_template(page_name)


@app.route('/submit_details', methods=['POST', 'GET'])
def submit_details():
    if request.method == 'POST':
        # data = request.form.to_dict()
        name = request.form['name']
        email = request.form['email_id']
        phone_no = request.form['phone_number']

        data = [name, email, phone_no]

        scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
                 "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

        credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
        client = gspread.authorize(credentials)

        sheet = client.open('Customer Details').sheet1

        sheet.append_row(data)

        return redirect('success.html')

    else:
        return 'Something went wrong. Please try again!'


# @app.route('/submit_details', methods=['POST', 'GET'])
# def submit_details():
#     if request.method == 'POST':
#         data = request.form.to_dict()
#         print(data)
#         write_to_csv(data)
#         return 'Form Submitted'
#     else:
#         return 'Something went wrong. Please try again!'


@app.route('/download')
def downloadFile():
    path = "CustomerDetails.csv"
    return send_file(path, as_attachment=True)


# @app.route('/delete')
# def downloadFile():
#     path = "CustomerDetails.csv"
#     return send_file(path, as_attachment=True)


def write_to_csv(data):
    with open('CustomerDetails.csv', mode='a') as database:
        fieldnames = ['name', 'email_id', 'phone_number']
        writer = csv.DictWriter(database, fieldnames=fieldnames)
        writer.writerow(data)


if __name__ == '__main__':
    app.run(debug=True)
