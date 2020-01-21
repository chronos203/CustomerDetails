from flask import Flask, render_template, redirect, request, send_file, url_for
import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/submit_details', methods=['POST', 'GET'])
def submit_details():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email_id']
        phone_no = request.form['phone_number']
        data = [name, email, phone_no]
        scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
                 "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
        credentials = ServiceAccountCredentials.from_json_keyfile_dict(create_credentials(), scope)
        client = gspread.authorize(credentials)
        sheet = client.open('Customer Details').sheet1
        sheet.append_row(data)
        return render_template('success.html', data=data)
    else:
        return 'Something went wrong. Please try again!'



def create_credentials():
    keys = {
      "type": "service_account",
      "project_id": "customerdetails-265613",
      "private_key_id": "ecf56ac799296d6cf9771f3b190b423477c435ec",
      "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCsxOMacsOzOZ97\nndCsJ9eYtWDqWbn/z+fqLSyqd8nG90Zcy4K4Z3zVbMGSWo5Kv6h0ne+HKkGHLEnO\nSTzY/nmuNhJeOfvKLhPYE1Tj1om2YCCivXJZDwqRl7/ZtS6Kc3CU39ePBRx+C2oH\nDtgPlMwiN4OY/MxYuhg9quEur0WWZ+dF1279g+vZyo7s4R6c5phRJ3ML7EoYr0le\nn++K0QSybq32AMF6C4u4mlQy5Cgaly8kjriNclhZTksovb/EvWQl6mqS5tji/AXH\nMDqsZctJRP/a/I8Fir7uHO8rq88wp+in6GkBYcD5TC2BfujSJLo0vUVDBmLHVmE5\nJ3jzra+jAgMBAAECggEAInOGZ9U/wgL5EvDm1hWBz/FHOKQYy3KdZ9yHPhzx7wuL\nC+EHGZeFVJfBx9nn6u7p/AssYvMhqv9BXnHLQOgJwpwEsKZ2V5w1l85PDLnQrz3e\n9CS74xd1P5AXkSWoeLJJXl5+gQX/ZwEGrQ6gNgcxZ5dTVhP++ahuQgnLqoAH69RL\nRaf235ReHDezLhqG63mu4X7JVRS5gBX7DQ/HoY/1kxecA1ZtgXjkWT9x6eC88eIr\nR+6QXYtQjQWXhTyxWgrzPRm2woUn7dw6wBo90STBO+oxczyccme/R4Ie812mHBZG\nR/naNCmhrRCWbiDomcpHEyp7l0vbLOuMbi8oaUApnQKBgQDgMsQhUrxxh6R2e4Ht\nrS+yCZxd3MatPKUCFJJ3IVp7qs8Fx0I6y6593bDQBHdglE4nVl1WMuDFdbe9DpwU\nVOKG5him1djJHkSzLdnh+NHexn7aPabMWmnaeVPi2pWjQxTo5t8SqmdzZlXC2SYt\nLc7yCb5goeEOyISAgrea+vPoNQKBgQDFRpcPG8YuZFTJv18cwnOsLz1gT5harndt\nGuyxrIjHoq/xd2a9nGH5eE4D1kzpUrl8/EJ6yf9l7OtlBG6zt+/WshzkOPAe5BC5\nnww0D/VkS3c0nwc75S1MaRUzlVVCPEGM2W6b/Qwm3zo+c1n7cJBCCuXX6SMB4d9g\nqfyDzgejdwKBgQCDJu95Fu9J8rGQ5htRsJhQLDMe7YID4ZAdsW8k5YwLABbvKGtj\n/bbrxn4ikhpLkzZM6MbdIBJBMOX1YNCJTEbf50bQghS5Qk2qC86D1IzhJ3kZrisf\nLFz0AznBYWFcCmf2/ufMAYdXCKxuuZ0NnNiM2opV+RyxCzgH/W/u55M7aQKBgHJ5\nBLzqo/RVmfG7z6gzmcWnX9kcNs8gAALapdBvyqr1V10pqP+L2DpXugV1/AlETIgf\nJUB1KHNvqCRlDwvQRybxEdzIwWVbd+0OQpmPTRjWxaROR3dVBBUbwQa+t8uIhY0C\nurFfhAamb/i/HM7PwZXhFwBTs1GrTOCdov6ktj//AoGBALnJwNb93azwfiRzCwww\nwVOkwWfm5hocAjl+DudVwiSG5DYBxxmG635GmtF8o8aR/z/vJ9RohKDWva14jtCJ\nPtWaIsPRVbeKYBIiwFC20RcrnCEpr62npQCX5rItFDJwdp91Fal/N2Zcl3pT1F2V\nWxbEVLAkkc9lc7iQLIin0MEd\n-----END PRIVATE KEY-----\n",
      "client_email": "legislator@customerdetails-265613.iam.gserviceaccount.com",
      "client_id": "110794449779001164442",
      "auth_uri": "https://accounts.google.com/o/oauth2/auth",
      "token_uri": "https://oauth2.googleapis.com/token",
      "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
      "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/legislator%40customerdetails-265613.iam.gserviceaccount.com"
    }
    return keys


if __name__ == '__main__':
    app.run(debug=True)


# @app.route('/submit_details', methods=['POST', 'GET'])
# def submit_details():
#     if request.method == 'POST':
#         data = request.form.to_dict()
#         print(data)
#         write_to_csv(data)
#         return 'Form Submitted'
#     else:
#         return 'Something went wrong. Please try again!'


# @app.route('/download')
# def downloadFile():
#     path = "CustomerDetails.csv"
#     return send_file(path, as_attachment=True)


# @app.route('/delete')
# def downloadFile():
#     path = "CustomerDetails.csv"
#     return send_file(path, as_attachment=True)


# def write_to_csv(data):
#     with open('CustomerDetails.csv', mode='a') as database:
#         fieldnames = ['name', 'email_id', 'phone_number']
#         writer = csv.DictWriter(database, fieldnames=fieldnames)
#         writer.writerow(data)


# @app.route('/<string:page_name>')
# def page_load(page_name):
#     return render_template(page_name)

