import sys
##sys.path.append("C:\github\personal-wallet\src")
from flask import Flask, jsonify, json, render_template, request, redirect
from wallet.config import engine
from sqlalchemy import select
from sqlalchemy.orm import Session
from wallet.models.registers import Category, Account
from wallet.adapter.orm import start_mapper

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movements.db"

session = Session(engine)
start_mapper()

@app.route('/')
def index():
    return "hello"

@app.route('/accounts', methods=['POST' , 'GET'])
def get_accounts():
    if request.method == 'POST':
        acc_name = request.form["name"]
        acc_type = request.form["type"]
        acc_balance = request.form["initial_balance"]
        new_acc = Account(acc_name , acc_type, acc_balance)
        try:
            session.add(new_acc)
            session.commit()
            return redirect('/accounts')
        except Exception as error:
            session.rollback()
            return str(error)
    else:
        accs = session.query(Account).all()
        return render_template("accounts.html", accounts = accs)



if __name__ == "__main__":
    app.run(debug=True , host="192.168.1.102")