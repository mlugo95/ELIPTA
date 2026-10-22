===========================================================
E.L.I.P.T.A. - Electronic Local Interface for Providers and Treatment Assessment
===========================================================

Version: 1.0.0
Author: Martin Lugo

-----------------------------------------------------------
1. DESCRIPTION
-----------------------------------------------------------

ELIPTA is an electronic health record (EHR) made using the 
Django REST Framework (DRF) designed to help healthcare 
providers manage patient records,prescriptions, 
laboratory results, and medical reports.

-----------------------------------------------------------
2. FEATURES
-----------------------------------------------------------

- Patient registration
- Patient search
- Medical notes
- Prescriptions
- Laboratory tests
- Imaging reports
- PDF report uploads/downloads
- User authentication
- Responsive interface
- Scheduling calendar

-----------------------------------------------------------
3. SYSTEM REQUIREMENTS
-----------------------------------------------------------

Operating System:
- Windows 10+
- Linux
- macOS

Software:
- Python 3.12+
- Django 5.x
- SQLite (default) or PostgreSQL
- pip

Optional:
- Virtual Environment (venv)

-----------------------------------------------------------
4. INSTALLATION
-----------------------------------------------------------

1. Create virtual environment

python -m venv venv

2. Activate environment

Windows:
venv\Scripts\activate

Linux/macOS:
source venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Run migrations

python manage.py migrate

5. Create administrator

python manage.py createsuperuser

6. Start server

python manage.py runserver

-----------------------------------------------------------
5. PROJECT STRUCTURE
-----------------------------------------------------------

project/

    app/
        models.py
        views.py
        forms.py
        urls.py

    templates/
    static/
    media/

-----------------------------------------------------------
6. CONFIGURATION
-----------------------------------------------------------

Edit settings.py if necessary.

Configure:

- SECRET_KEY
- DEBUG
- ALLOWED_HOSTS
- DATABASE
- MEDIA_ROOT
- STATIC_ROOT

-----------------------------------------------------------
7. HOW TO USE
-----------------------------------------------------------

1. Login.
2. Create or edit a patient.
3. Open the patient's profile.
4. Add or edit notes.
5. Add or edit prescriptions.
6. Upload/download laboratory results.
7. Upload/dpwnload reports.

-----------------------------------------------------------
8. DEPENDENCIES
-----------------------------------------------------------

- Python 3.13.14 or most recent versions
- Django
- Pillow
- WeasyPrint (if generating PDFs)
- PIP

-----------------------------------------------------------
9. KNOWN ISSUES
-----------------------------------------------------------

- Large PDF uploads may take several seconds.
- Internet Explorer is not supported.

-----------------------------------------------------------
10. FUTURE IMPROVEMENTS
-----------------------------------------------------------

- Email notifications
- Dark mode

-----------------------------------------------------------
11. CONTACT
-----------------------------------------------------------

Developer: Martin Lugo
Email: maenlume95@gmail.com
