from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import bcrypt
import secrets
from config import STATIC_URL_PREFIX



app = Flask(__name__, static_url_path='/static', static_folder='static')

app = Flask(__name__)

# MySQL Configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="dagwapan0810",
    database="myappdb"
)

#home page
@app.route('/')
def index():
    return render_template('index.html')

#about us page
@app.route('/about')
def about():
    return render_template('about.html')

#services us page
@app.route('/services')
def services():
    return render_template('services.html')

#contact us page
@app.route('/contact')
def contact():
    return render_template('contact.html')

#testimonies page
@app.route('/testimonies')
def testimonies():
    return render_template('testimonies.html')

#admissions page
@app.route('/admissions')
def admissions():
    return render_template('admissions.html')

#login page
@app.route('/login')
def login():
    return render_template('login.html')

#studentportal page
@app.route('/studentportal')
def studentportal():
    return render_template('studentportal.html')

#events page
@app.route('/events')
def events():
    return render_template('events.html')

#early school page
@app.route('/early')
def early():
    return render_template('early.html')

#primary school page
@app.route('/primary')
def primary():
    return render_template('primary.html')

#lowersecondary school page
@app.route('/lowersecondary')
def lowersecondary():
    return render_template('lowersecondary.html')

#accademicexcellence school page
@app.route('/accademicexcellence')
def accademicexcellence():
    return render_template('accademicexcellence.html')

#principal welcome message school page
@app.route('/principal_welcome_message')
def principal_welcome_message():
    return render_template('principal_welcome_message.html')

#academicsuccess page
@app.route('/academicsuccess')
def academicsuccess():
    return render_template('academicsuccess.html')

#best_universities page
@app.route('/best_universities')
def best_universities():
    return render_template('best_universities.html')

#trip page
@app.route('/trip')
def trip():
    return render_template('trip.html')

#studentsupport page
@app.route('/studentsupport')
def studentsupport():
    return render_template('studentsupport.html')

#dnpschallenge page
@app.route('/dnschallenge')
def dnpschallenge():
    return render_template('dnpschallenge.html')

#application_requirments page
@app.route('/application_requirments')
def application_requirments():
    return render_template('application_requirments.html')

#application page
@app.route('/application')
def application():
    return render_template('application.html')

#tuition_fees page
@app.route('/tuition_fees')
def tuition_fees():
    return render_template('tuition_fees.html')


@app.route('/schoo_calendar_dnps')
def schoo_calendar_dnps():
    return render_template('schoo_calendar_dnps.pdf')
@app.route('/add_to_calendar')
def add_to_calendar():
    return render_template('add_to_calendar.ics')

#more_faq page
@app.route('/more_faq')
def more_faq():
    return render_template('more_faq.html')

#meal-services page
@app.route('/meal_services')
def meal_services():
    return render_template('meal_services.html')

#online_payment page
@app.route('/online_payment')
def online_payment():
    return render_template('online_payment.html')

#teacher_nomination page
@app.route('/teacher_nomination')
def teacher_nomination():
    return render_template('teacher_nomination.html')

#enquiry page
@app.route('/enquiry')
def enquiry():
    return render_template('enquiry.html')

#create-account
@app.route('/create_accoun')
def create_account():
    return render_template('create_account.html')

#route for account registration
@app.route('/auth/register', methods=['POST'])
def register():
    # Get form data
    firstName = request.form['firstName']
    lastName = request.form['lastName']
    otherName = request.form['otherName']
    contactAddress = request.form['contactAddress']
    permanentAddress = request.form['permanenttAddress']
    nationality = request.form['nationality']
    stateOfOrigin = request.form['state']
    lga = request.form['lga']
    province = request.form['kubwa']
    zipCode = request.form['zipCode']
    phoneNumber = request.form['phone']
    email = request.form['email']
    retypeEmail = request.form['retypeEmail']
    password = request.form['password']
    retypePassword = request.form['retypePassword']
   

    try:
        # Hash password
        salt = bcrypt.gensalt(10)
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

        cursor = db.cursor()

        # Insert data into MySQL
        query = "INSERT INTO users (firstName, lastName, otherName, contactAddress, permanentAddress, nationality, stateOfOrigin, lga, province, zipCode, phoneNumber, email, retypeEmail, password,  retypePassword) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (firstName, lastName, otherName, contactAddress, permanentAddress, nationality, stateOfOrigin, lga, province, zipCode, phoneNumber, email, retypeEmail, password,  retypePassword)
        cursor.execute(query, values)

        db.commit()
        cursor.close()

        return redirect(url_for('success'))
    except Exception as e:
        print(e)
        db.rollback()
        return redirect(url_for('error'))

@app.route('/success')
def success():
    return "Account created successfully!"

@app.route('/error')
def error():
    return "An error occurred while creating an account. Please try again."




if __name__ == '__main__':
    app.run(debug=True)
