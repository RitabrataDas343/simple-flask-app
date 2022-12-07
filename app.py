from flask import Flask, render_template
from threading import Thread
import requests
import schedule

app = Flask(  
	__name__,
	template_folder='templates',  
	static_folder='static'  
)

l = list()

def run():
	app.run(host='0.0.0.0',port=8000)

def keep_alive(): 
    t = Thread(target=run)
    t.start()

def send_request():
    URL = "https://github-readme-activity-graph.ritabratadas1.repl.co"
    r = requests.get(url = URL)
    if (len(l) == 5):
        l.clear()
    l.append(r.status_code)

@app.route('/')
def home():
    keep_alive()
    schedule.every(5).seconds.do(send_request)
    schedule.run_pending()
    return render_template('base.html', l = l, length = len(l))
