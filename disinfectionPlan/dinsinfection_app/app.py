from flask import Blueprint , jsonify , request

app_bp = Blueprint('app', __name__)
@app_bp.route('/myApp' , methods=['POST'])
def myApp():
    #--------------Write your code here--------------#
    pass