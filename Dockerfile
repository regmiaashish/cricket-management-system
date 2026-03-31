# Use an official lightweight Python image
FROM python:3.11-slim

# Set environment variables
# PYTHONDONTWRITEBYTECODE: Prevents Python from writing pyc files to disc
# PYTHONUNBUFFERED: Prevents Python from buffering stdout and stderr
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8080

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
# These are required to build some Python packages (like psycopg2, mysqlclient, pillow, etc.)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    default-libmysqlclient-dev \
    pkg-config \
    zlib1g-dev \
    libjpeg-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the entire project into the working directory
COPY . /app/

# Run collectstatic to gather static files
# We pass a dummy SECRET_KEY here just in case settings.py requires one during collectstatic
RUN SECRET_KEY=dummy python manage.py collectstatic --noinput

# Expose the port the app runs on (Cloud Run uses 8080 by default)
EXPOSE 8080

# Command to run the application using Gunicorn
# Using 1 worker and 4 threads as a sensible default for Cloud Run
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "1", "--threads", "4", "core.wsgi:application"]
