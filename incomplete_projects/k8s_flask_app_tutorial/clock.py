from datetime import datetime
from flask import Flask
import pytz
app = Flask('clock')

timezone = pytz.timezone('America/New_York')

@app.route('/')
def index():
    now_utc = pytz.utc.localize(datetime.utcnow())
    now_ny = now_utc.astimezone(timezone)
    return "In Mardela Springs it is currently " now_nyc.strftime('%H:%M:%S')
    