import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(credentials)

sheet = client.open('Customer Details').sheet1

insertData = ['Abc', 'abc@abc.com', 123]
sheet.append_row(insertData)

details = sheet.get_all_records()
pprint(details)
