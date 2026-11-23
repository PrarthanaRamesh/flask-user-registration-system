# Flask User Registration & Document Management System

A full-stack web application built using **Python, Flask, SQLite, HTML, CSS and JavaScript** to collect, validate and store user information through a structured registration form, with support for document uploads.

## Overview

Managing user information through unstructured forms can make data collection and storage difficult. This project provides a centralized web-based solution that allows users to submit personal, demographic and educational information through an organized interface.

The application processes form submissions using Flask, stores structured records in an SQLite database and supports PDF and image uploads.

## Features

- **Structured Information Collection:** Collects personal details including name, email, phone number, date of birth and address.
- **Dynamic Location Selection:** Automatically populates state options based on the selected country using JavaScript.
- **Demographic Information:** Captures gender, education level and user interests.
- **Document Upload:** Supports PDF, JPG, JPEG and PNG file uploads.
- **Input Validation:** Implements required-field validation, email input validation, phone-number filtering and date-of-birth restrictions.
- **Database Management:** Stores submitted user information in an SQLite database with automatically generated record IDs.
- **Responsive Interface:** Uses CSS styling to provide a structured form layout.

## Tech Stack

| Category | Technologies |
|---|---|
| Backend | Python, Flask |
| Frontend | HTML5, CSS3, JavaScript |
| Database | SQLite |
| File Handling | Werkzeug |
| Development Tools | VS Code, Git, GitHub |

## Application Architecture

The application follows a simple client-server architecture.

1. **Frontend:** HTML provides the registration form, while CSS and JavaScript handle styling and client-side interactions.
2. **Backend:** Flask receives form submissions through HTTP POST requests, processes the submitted information and handles uploaded files.
3. **Database:** SQLite stores user records in a structured relational table.
4. **File Storage:** Uploaded documents are stored locally in the uploads directory.

### Project Structure

```text
flask-user-registration-system/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── static/
│   ├── style.css
│   └── script.js
│
└── templates/
    └── form.html
```

The SQLite database and uploaded documents are generated locally and excluded from version control.

## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/PrarthanaRamesh/flask-user-registration-system.git
```

### 2. Navigate to the project directory

```bash
cd flask-user-registration-system
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
.venv\Scripts\activate
```

**macOS / Linux:**

```bash
source .venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python app.py
```

### 7. Open in your browser

Navigate to:

```text
http://127.0.0.1:5000/
```

The SQLite database and required database table are initialized automatically when the application starts.

## Database Schema

The application uses an SQLite table named `users` with the following fields:

| Field | Description |
|---|---|
| id | Auto-incremented primary key |
| name | User's name |
| email | Email address |
| phone | Phone number |
| dob | Date of birth |
| address | Residential address |
| country | Selected country |
| state | Selected state |
| gender | Gender |
| education | Education level |
| interests | Selected interests |
| transcript_filename | Uploaded document filename |

## Current Limitations & Future Improvements

- Implement stronger server-side validation and form security.
- Add unique filename generation to prevent upload collisions.
- Introduce file-size limits and enhanced document validation.
- Implement CSRF protection.
- Add success and error feedback after form submission.
- Introduce an administrative dashboard for viewing and managing submitted records.
- Explore deployment with a production-ready database and secure file storage.

## Privacy & Security

This project is intended as a learning and portfolio demonstration.

- User-uploaded documents and the local SQLite database are excluded from version control.
- The application should use fictional test information during demonstrations.
- Additional security measures are required before accepting real personal information or deploying publicly.

## Author

**Prarthana Ramesh**

B.Tech Computer Science and Engineering (AI & ML)

- GitHub: [@PrarthanaRamesh](https://github.com/PrarthanaRamesh)

---

*Built as a hands-on full-stack development project to explore web application development, database integration and file handling using Flask.*