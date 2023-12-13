import psutil
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	cpu_percentage = psutil.cpu_percent()
	mem_percentage = psutil.virtual_memory().percent
	Message = None
	if cpu_percentage > 80 or mem_percentage > 80:
		Message = "High CPU or Memory Utilization detected. Please Scale up"
	return render_template("index.html", cpu_percentage=cpu_percentage, mem_percentage=mem_percentage, message=Message)
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
