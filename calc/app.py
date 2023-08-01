from flask import Flask, request

app = Flask(__name__)
# Simple calculator
"""Basic math operations."""
@app.route("/add")
def get_a_and_b():
    """Get the value of a and b."""
    a =request.args["a"]
    b= request.args["b"]
    aNum= int(a)
    bNum = int(b)
    return add(aNum,bNum)

def add(a,b):
    """Add a and b."""
    return str(a+b)

@app.route("/sub")
def getab():
    """Get the value of a and b."""
    a =request.args["a"]
    b= request.args["b"]
    aNum= int(a)
    bNum = int(b)
    return sub(aNum,bNum)
def sub(a,b):
   """Substract b from a."""
   return str(a - b)

@app.route("/mult")
def get_a_b():
    """Get the value of a and b."""
    a =request.args["a"]
    b= request.args["b"]
    aNum= int(a)
    bNum = int(b)
    return mult(aNum,bNum)
def mult(a, b):
    """Multiply a and b."""
    return str(a * b)

@app.route("/div")
def get_ab():
    """Get the value of a and b."""
    a =request.args["a"]
    b= request.args["b"]
    aNum= int(a)
    bNum = int(b)
    return div(aNum,bNum)
def div(a, b):
    """Divide a by b."""
    return str(a / b) 

@app.route("/math/<calculation>")
def calc(calculation):
    """"Mini caclulator for add, sub, duv and mult."""
    a =request.args["a"]
    b= request.args["b"]
    aN =int(a)
    bN = int(b)
    dictionary1 ={
        "add" : aN +bN, 
        "sub": aN -bN,
        "mult" : aN*bN,
        "div": aN/bN
    }
    final_calc = dictionary1[calculation]
    return str(final_calc)
