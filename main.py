from flask import Flask, request
from handler.parts import PartHandelr

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello World"

@app.route('/login')
def login():
    return "No Login  for you!!!"

@app.route('/PartApp/parts')
def parts():
    if request.args:
        return PartHandelr().searchParts(request.args)
    else:
        handler = PartHandelr()
        return handler.getAllParts()

@app.route('/PartApp/parts/<int:pid>')
def getPartById(pid):
    return PartHandelr().getPartById(pid)

@app.route('/PartApp/parts/<int:pid>/suppliers')
def getSuppliersPartById(pid):
    return PartHandelr().getSuppliersByPartId(pid)
if __name__ == '__main__':
    app.run()