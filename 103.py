import gspread
import subprocess
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials
import psutil


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

CPU=psutil.cpu_percent(interval=None, percpu=False)
TIME=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
SYNC=subprocess.check_output("~/net.ton.dev/scripts//check_node_sync_status.sh | grep TIME_DIFF | awk '{print $4}' | tr '[:upper:]' '[:lower:]'",shell=True)
RAM=psutil.virtual_memory()
worksheet.update_acell('B4', TIME),('C4', SYNC)
