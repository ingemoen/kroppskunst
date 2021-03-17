from flask import Blueprint, render_template

about = Blueprint('about', __name__, template_folder='templates')

@about.route('/')
@about.route('/us')
def index():
    return render_template('us.html')

@about.route('/faq')
def faq():
    return render_template('faq.html')

@about.route('/privacy')
def privacy():
    return render_template('privacy.html')

@about.route('/returns')
def returns():
    return render_template('returns.html')

@about.route('/sizes')
def sizes():
    return render_template('sizes.html')

@about.route('/tc')
def tc():
    return render_template('tc.html')

@about.route('/warranty')
def warranty():
    return render_template('warranty.html')


