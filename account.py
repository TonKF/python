import gspread
import subprocess

from oauth2client.service_account import ServiceAccountCredentials
scope = [
'https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive',
]
json_file_name = 'py.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
gc = gspread.authorize(credentials)
spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1bn_3dljif7wb4IDjwUe34TSSOuqZ6w7Zcgb-8OSafNI/edit#gid=0'

doc = gc.open_by_url(spreadsheet_url)

worksheet = doc.worksheet('sheet1')

RAW = subprocess.check_output("cat ~/python/raw.log",shell=True)
