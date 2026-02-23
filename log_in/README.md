# Auth Demo (Django)

## Features
- Sign up at `/signup/`
- Login at `/login/`
- Logout at `/logout/`
- Email verification link at `/verify-email/<uid>/<token>/`
- Django admin at `/admin/`

## Tech stack
- Python 3.9
- Django 4.2
- SQLite (`db.sqlite3`)
- Bootstrap 5 (CDN)
- `django-simple-captcha`
- `python-decouple`

## Project structure
- `log_in/` — project configuration (`settings.py`, `urls.py`, `forms.py`, templates)
- `log_in_app/` — app logic (`views.py`, admin configuration)
- `manage.py` — Django command entrypoint
- `requirements.txt` — Python dependencies

## Quick start
1. Activate virtual environment:
   - macOS/Linux: `source env/bin/activate`
2. Install dependencies:
   - `pip install -r requirements.txt`
3. Apply migrations:
   - `python manage.py migrate`
4. Run server:
   - `python manage.py runserver`

Open: `http://127.0.0.1:8000/`

## Environment variables
Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

# Email
EMAIL_BACKEND=console
EMAIL_HOST=smtp.gmail.com
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
```

Notes:
- Use `EMAIL_BACKEND=console` in development (verification email appears in terminal).
- For real emails, configure SMTP credentials.

## Authentication flow
1. User creates account at `/signup/`.
2. Account is saved as inactive.
3. Verification email is sent.
4. User clicks verification link.
5. Account becomes active and user can log in.

## Useful commands
- Check project health: `python manage.py check`
- Run tests: `python manage.py test`
- Create admin user: `python manage.py createsuperuser`

## Current status
- Core auth + email verification + CAPTCHA are working.
- Automated tests are not implemented yet (`0` tests currently).
