from secrets import token_bytes
from flask import Flask, render_template, request, flash, session 

from modules.webhelper.backend import CostCalculator

#Flask App Setup
app = Flask(__name__)

def generate_secret():
    if app.secret_key == None:
        app.secret_key = token_bytes(128)

@app.route("/")
def home():
    return render_template('homepage.html')

@app.route("/calculation", methods=["GET", "POST"])
def calculation():
    generate_secret()
    app_runner = CostCalculator()
    prices = app_runner.get_prices()
    if request.method == "POST":
        try:
            containertype = request.form.get("Container Type")
            cpu = int(request.form.get("cpu"))
            ram = float(request.form.get("ram"))
            storage = float(request.form.get("storage"))
            backup = request.form.get("option")
            containernumber = int(request.form.get("ContainerNumber"))
            session["inputs"] = [
                {
                    'containertype': containertype,
                    'cpu': cpu,
                    'ram': ram,
                    'storage': storage,
                    'backup': backup,
                    'containernumber': containernumber
                }
            ]
            session["data"] = app_runner.get_outputs(containertype, cpu, ram, storage, backup, containernumber)
            return render_template("calculation.html", data=session['data'], inputs=session['inputs'], prices=prices)
        except Exception as e:
            print(e)
            flash("You have submitted blank data!")
    return render_template("calculation.html", prices=prices)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)