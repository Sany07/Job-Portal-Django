# Job Portal
Django Job Portal.   

## Installation 

```
open terminal and type
https://github.com/Sany07/Job-Portal.git

or simply download using the url below
https://github.com/Sany07/Job-Portal.git
```

## Install requirements

```
pip install -r requirements.txt
```
## Database

```
Set the database from settings.py
```

## To migrate the database open terminal in project directory and type
```
python manage.py makemigrations
python manage.py migrate
```

## Collects all static files in your apps

```
python manage.py collectstatic
```

## Run the server
```
python manage.py runserver
```

![Settings Window](https://raw.github.com/Sany07/Django-Job-Portal/master/screenshots/screencapture-127-0-0-1-8000-2020-05-08-17_03_46.png)

![Settings Window](https://raw.github.com/Sany07/Django-Job-Portal/master/screenshots/screencapture-127-0-0-1-8000-jobs-2020-05-08-17_40_01.png)

![Settings Window](https://raw.github.com/Sany07/Django-Job-Portal/master/screenshots/screencapture-127-0-0-1-8000-job-79-2020-05-08-16_59_55.png)

![Settings Window](https://raw.github.com/Sany07/Django-Job-Portal/master/screenshots/screencapture-127-0-0-1-8000-job-create-2020-05-08-17_00_46.png)

![Settings Window](https://raw.github.com/Sany07/Django-Job-Portal/master/screenshots/screencapture-127-0-0-1-8000-dashboard-2020-05-08-17_01_07.png)

![Settings Window](https://raw.github.com/Sany07/Django-Job-Portal/master/screenshots/screencapture-127-0-0-1-8000-dashboard-employer-job-54-applicants-2020-05-08-17_01_34.png)

## Troubleshooting ✅

- **Virtualenv error: "ensurepip is not available"** — On Debian/Ubuntu you may see "The virtual environment was not created successfully because ensurepip is not available." Fix by installing the venv package and recreating the environment:

```bash
sudo apt update && sudo apt install -y python3-venv python3.12-venv
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
```

- **psycopg2 build error** — If building `psycopg2` fails locally (C-extensions), either install system headers (`libpq-dev`) to build from source or use `psycopg2-binary` for local development. Example:

```bash
sudo apt install -y libpq-dev build-essential
# or (for local dev)
pip install psycopg2-binary
```

> Note: For production, prefer `psycopg2` built against system libraries instead of `psycopg2-binary`.

<div align="center">
    <h3>========Thank You=========</h3>
</div>

