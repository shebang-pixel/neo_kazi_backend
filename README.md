# Neo Kazi Backend

Backend services for neo kazi - a service marketplace platform built with Django and Django REST Framework.

## Overview

Neo Kazi Backend is a robust RESTful API that powers the neo kazi service marketplace. It provides comprehensive endpoints for managing users, services, bookings, reviews, invoices, payments, and categories.

## Technology Stack

- **Python 3.x**
- **Django** - Web framework
- **Django REST Framework** - REST API framework
- **Database** - Compatible with PostgreSQL/SQLite

## Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (venv)

### Step 1: Clone the Repository

```bash
git clone https://github.com/shebang-pixel/neo_kazi_backend.git
cd neo_kazi_backend
```

### Step 2: Create and Activate Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run Migrations

```bash
python manage.py migrate
```

### Step 5: Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### Step 6: Run Development Server

```bash
python manage.py runserver 0.0.0.0:8000
```

The API will be accessible at `http://0.0.0.0:8000`

## API Endpoints

### Core Resources

| Resource | Collection URL (GET/POST) | Detail URL (GET/PUT/PATCH/DELETE) |
|----------|---------------------------|-----------------------------------|
| Users | `/api/users/` | `/api/users/{id}/` |
| Services | `/api/services/` | `/api/services/{id}/` |
| Bookings | `/api/bookings/` | `/api/bookings/{id}/` |
| Reviews | `/api/reviews/` | `/api/reviews/{id}/` |
| Invoices | `/api/invoices/` | `/api/invoices/{id}/` |
| Payments | `/api/payments/` | `/api/payments/{id}/` |
| Categories | `/api/categories/` | `/api/categories/{id}/` |

### Filtering and Searching

#### Services
```bash
# Filter by category and provider
GET /api/services/?category={id}&provider={id}&is_active=true

# Search by keyword
GET /api/services/?search=plumbing

# Order results (ascending or descending)
GET /api/services/?ordering=-price        # descending price
GET /api/services/?ordering=created_at    # ascending creation date
```

#### Bookings
```bash
# Filter by status and user
GET /api/bookings/?status=PENDING&user={id}

# Search by location or description
GET /api/bookings/?search=Nairobi

# Order by scheduled date
GET /api/bookings/?ordering=scheduled_at
```

#### Users
```bash
# Filter by role and city
GET /api/users/?role=PROVIDER&city=Nairobi

# Search by email or name
GET /api/users/?search=john@example.com
```

#### Invoices
```bash
# Filter by payment status
GET /api/invoices/?payment_status=paid

# Search by invoice number or transaction ID
GET /api/invoices/?search=TRX12345
```

## Project Structure

```
neo_kazi_backend/
├── manage.py
├── requirements.txt
├── venv/
└── [Django app directories]
```

## Environment Variables

Create a `.env` file in the project root if needed for environment-specific settings:

```bash
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=your-database-url
```

## Common Commands

```bash
# Create a new Django app
python manage.py startapp app_name

# Make migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Run tests
python manage.py test

# Create superuser
python manage.py createsuperuser

# Access Django shell
python manage.py shell

# Collect static files
python manage.py collectstatic
```

## API Documentation

Once the server is running, access the API documentation at:
- **DRF Browsable API**: `http://0.0.0.0:8000/api/`
- **Django Admin**: `http://0.0.0.0:8000/admin/`

## Contributing

1. Create a new branch for your feature
2. Make your changes and commit them
3. Push to the repository
4. Create a Pull Request

## License

[Add your license here]

## Support

For issues or questions, please open an issue on the GitHub repository.
