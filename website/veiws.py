from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .calculator import calculate_compost_ratios

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('index.html')

@views.route('/get_started')
def get_started():
    return render_template("get_started.html")

@views.route('/contact')
def contact():
    return render_template("contact.html")

@views.route('/about')
def about():
    return render_template("about.html")

@views.route('/calculate', methods=['GET', 'POST'])
def calculate():
    output = request.form.to_dict()
    result = calculate_compost_ratios(output["waste-type"], int(output["waste-size"]), int(output["duration"]))
    return render_template("get_started.html", result=result)


