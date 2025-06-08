# Job Portal
Django Job Portal - A full-featured job listing and application platform with Docker and Kubernetes support.

## Table of Contents
- [Local Installation](#local-installation)
- [Docker Deployment](#docker-deployment)
- [Kubernetes Deployment](#kubernetes-deployment)
- [Features](#features)

## Local Installation

```bash
# Clone the repository
git clone https://github.com/Sany07/Job-Portal.git

# Navigate to the project directory
cd Job-Portal-Django
```

## Install requirements

```bash
pip install -r requirements.txt
```

## Database

```
Set the database from settings.py
```

## To migrate the database open terminal in project directory and type
```bash
python manage.py makemigrations
python manage.py migrate
```

## Collects all static files in your apps

```bash
python manage.py collectstatic
```

## Run the server locally
```bash
python manage.py runserver
```

## Docker Deployment

The application can be easily deployed using Docker:

```bash
# Build the Docker image
docker build -t job-portal:latest .

# Run the Docker container
docker run -p 8000:8000 job-portal:latest
```

## Kubernetes Deployment

This project includes Kubernetes manifests for deployment in a Kubernetes cluster:

```bash
# Create the namespace
kubectl apply -f k8s/namespace.yaml

# Deploy PostgreSQL database
kubectl apply -f k8s/persistent-volume.yaml
kubectl apply -f k8s/persistant-volume-claim.yaml
kubectl apply -f k8s/postgres-deployment.yaml
kubectl apply -f k8s/postgres-service.yaml

# Deploy Django application
kubectl apply -f k8s/django-deployment.yaml
kubectl apply -f k8s/django-service.yaml

# Set up ingress (if using)
kubectl apply -f k8s/ingress.yaml
```

### Kubernetes Configuration

The Kubernetes deployment includes:
- Separate namespace for the application (`django-app`)
- PostgreSQL database with persistent storage
- Django web application with environment variables for database connection
- Services for both Django and PostgreSQL
- Ingress configuration for external access

![Settings Window](https://raw.github.com/Sany07/Django-Job-Portal/master/screenshots/screencapture-127-0-0-1-8000-2020-05-08-17_03_46.png)

![Settings Window](https://raw.github.com/Sany07/Django-Job-Portal/master/screenshots/screencapture-127-0-0-1-8000-jobs-2020-05-08-17_40_01.png)

![Settings Window](https://raw.github.com/Sany07/Django-Job-Portal/master/screenshots/screencapture-127-0-0-1-8000-job-79-2020-05-08-16_59_55.png)

![Settings Window](https://raw.github.com/Sany07/Django-Job-Portal/master/screenshots/screencapture-127-0-0-1-8000-job-create-2020-05-08-17_00_46.png)

![Settings Window](https://raw.github.com/Sany07/Django-Job-Portal/master/screenshots/screencapture-127-0-0-1-8000-dashboard-2020-05-08-17_01_07.png)

![Settings Window](https://raw.github.com/Sany07/Django-Job-Portal/master/screenshots/screencapture-127-0-0-1-8000-dashboard-employer-job-54-applicants-2020-05-08-17_01_34.png)

## Features
- User authentication system (Login, Register, Password Reset)
- Employer and Employee user types
- Job posting and management for employers
- Job search and application for employees
- Dashboard for both employer and employee
- Containerized application with Docker
- Complete Kubernetes deployment configuration
- PostgreSQL database integration

## Technologies Used
- Django
- PostgreSQL
- Docker
- Kubernetes
- HTML/CSS/JavaScript
- Bootstrap

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

<div align="center">
    <h3>========Thank You=========</h3>
</div>

