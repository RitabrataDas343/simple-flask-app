from flask import Flask, render_template
from threading import Thread
import schedule
import os

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
    hostname = "github-readme-activity-graph.ritabratadas1.repl.co" 
    response = os.system("ping -c 1 " + hostname)
    if (len(l) == 5):
        l.clear()
    if response == 0:
        l.append(200)
    else:
        l.append(500)

@app.route('/')
def home():
    keep_alive()
    schedule.every(5).seconds.do(send_request)
    schedule.run_pending()
    return render_template('base.html', l = l, length = len(l))

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8000)