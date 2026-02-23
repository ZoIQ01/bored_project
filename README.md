# Activity Manager

A Django web application that helps you discover and manage interesting activities. The app imports activities from the [Bored API](https://www.boredapi.com/) and provides features to browse, filter, sort, and get random activity suggestions.

## Features

- **Activity Import**: Fetch activities from the Bored API via web interface or management command
- **Browse Activities**: View all activities in a paginated list
- **Filter & Sort**: Filter activities by type, participants, price, and accessibility
- **Random Activity**: Get random activity suggestions when you're looking for something to do
- **Activity Details**: View detailed information about each activity including type, participants, price, and accessibility

## Activity Types

The app supports the following activity categories:
- Education
- Recreational
- Social
- DIY
- Charity
- Cooking
- Relaxation
- Music
- Busywork

## Tech Stack

- **Framework**: Django 4.2
- **Database**: SQLite3
- **Python**: 3.x
- **Key Dependencies**:
  - django-filter (filtering capabilities)
  - requests (API integration)
  - python-dotenv (environment configuration)

## Installation

### Prerequisites

- Python 3.x
- pip

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd git_repo
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   
   Create a `.env` file in the project root:
   ```env
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```

5. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

6. **Import initial activities** (optional)
   ```bash
   python manage.py import_activity
   ```

7. **Create a superuser** (optional, for admin access)
   ```bash
   python manage.py createsuperuser
   ```

8. **Start the development server**
   ```bash
   python manage.py runserver
   ```

9. **Access the application**
   
   Open your browser and navigate to `http://127.0.0.1:8000/`

## Usage

### Web Interface

- **Home Page**: `/` - Landing page with navigation
- **Activities List**: `/activities/` - Browse all activities with filtering and sorting options
- **Random Activity**: `/activities/random/` - Get a random activity suggestion
- **Import Activities**: `/activities/import/` - Import new activities from the API
- **Activity Details**: `/activities/<id>/` - View details of a specific activity

### Management Commands

Import activities from the Bored API:
```bash
python manage.py import_activity
```

This command imports up to 100 activities with a 5-second timeout.

### Admin Interface

Access the Django admin panel at `/admin/` to manage activities directly:
```bash
python manage.py createsuperuser  # Create admin account first
```

## Project Structure

```
git_repo/
├── manage.py                     # Django management script
├── requirements.txt              # Python dependencies
├── db.sqlite3                    # SQLite database
├── activities/                   # Main application
│   ├── models.py                 # Database models (Activity)
│   ├── views/                    # View controllers
│   │   ├── home_view.py
│   │   ├── table_view.py
│   │   ├── random_view.py
│   │   ├── import_view.py
│   │   └── show_detail_view.py
│   ├── services/                 # Business logic
│   │   ├── import_from_api.py    # API import service
│   │   ├── get_rdm_activity.py   # Random activity logic
│   │   └── activity_cache.py     # Caching utilities
│   ├── templates/                # HTML templates
│   ├── management/commands/      # Custom Django commands
│   │   └── import_activity.py
│   ├── tests/                    # Test suite
│   └── migrations/               # Database migrations
└── core/                         # Project settings
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

## Testing

Run the test suite:
```bash
python manage.py test activities
```

Test modules include:
- `test_import.py` - Tests for activity import functionality
- `test_filter.py` - Tests for filtering activities
- `test_sort.py` - Tests for sorting activities
- `test_random.py` - Tests for random activity selection

## Configuration

### Environment Variables

Create a `.env` file with the following variables:

| Variable | Description | Default |
|----------|-------------|---------|
| `SECRET_KEY` | Django secret key (required) | - |
| `DEBUG` | Enable debug mode | `False` |
| `ALLOWED_HOSTS` | Comma-separated list of allowed hosts | - |

### API Configuration

The app uses the Bored API at `https://bored-api.appbrewery.com/random`. Configuration constants can be found in `activities/const.py`:

- `BORED_API_URL`: API endpoint
- `DEFAULT_IMPORT_TIMEOUT`: API call timeout (5 seconds)
- `DEFAULT_IMPORT_COUNT`: Default number of activities to import (20)
- `MAX_IMPORT_COUNT`: Maximum activities per import batch (100)

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

## License

This project is available for educational and personal use.

## Acknowledgments

- Activity data provided by [Bored API](https://www.boredapi.com/)
- Built with [Django](https://www.djangoproject.com/)
