from flask import Blueprint, render_template, session, redirect, url_for, request, flash, g, jsonify, abort
#from flask_login import requires_login

api_orders = Blueprint('api_orders', __name__)

@api_orders.route('/')
def index():
    pass

@api_orders.route('/new', methods=['GET', 'POST'])
def new():
    pass

@api_orders.route('/edit', methods=['GET', 'POST'])
def edit():
    pass
