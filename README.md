# Late Show Code Challenge



## Setup

1. Clone the repository:
```bash
git clone git@github.com:30010275/late-show-code-chalenge-p4.git
cd late-show-code-chalenge-p4
```

2. Install dependencies:
```bash
pipenv install
```

3. Set up the database:
```bash
pipenv run flask db upgrade
pipenv run python seed.py
```

4. Run the application:
```bash
pipenv run flask run
```

## enviroment setup

Environment variables can be set in the `.env` file:
```
FLASK_APP=app.py
FLASK_ENV=development
DATABASE_URL=sqlite:///instance/lateshow.db
```

## Database Migrations

To create a new migration:
```bash
pipenv run flask db migrate -m "your migration message"
```

To apply migrations:
```bash
pipenv run flask db upgrade
