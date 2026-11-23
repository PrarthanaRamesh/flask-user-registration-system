from flask import Flask, render_template, request, redirect
import sqlite3
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)


UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"pdf", "jpg", "jpeg", "png"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS



def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn



def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            dob TEXT NOT NULL,
            address TEXT NOT NULL,
            country TEXT NOT NULL,
            state TEXT NOT NULL,
            gender TEXT NOT NULL,
            education TEXT NOT NULL,
            interests TEXT,
            transcript_filename TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

create_table()



@app.route("/")
def index():
    return render_template("form.html")


@app.route("/submit", methods=["POST"])
def submit():
   
    name = request.form.get("name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    dob = request.form.get("dob")
    address = request.form.get("address")
    country = request.form.get("country")
    state = request.form.get("state")
    gender = request.form.get("gender")
    education = request.form.get("education")
    interests_list = request.form.getlist("interests")

    interests = ", ".join(interests_list)

    
    file = request.files.get("transcript")

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
    else:
        return "Invalid file type. Only PDF and images allowed."

   
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO users (
            name, email, phone, dob, address,
            country, state, gender, education,
            interests, transcript_filename
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        name, email, phone, dob, address,
        country, state, gender, education,
        interests, filename
    ))

    conn.commit()
    conn.close()

    return redirect("/")



if __name__ == "__main__":
    app.run(debug=False)
