import sys
##sys.path.append("C:\github\personal-wallet\src")
from flask import Flask, jsonify, json
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

@app.route('/accounts')
def get_accounts():
    accs = session.scalars(select(Account))
    return json.dumps([ (row.id, row.name) for row in accs ])



if __name__ == "__main__":
    app.run(debug=True , host="192.168.1.102")