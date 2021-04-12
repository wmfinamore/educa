# Dockefile

# pull base image
FROM python:3.9


# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=educa.settings.pro

# Set work directory
WORKDIR /code


# Install dependencies
RUN pip install pipenv
COPY Pipfile Pipfile.lock /code/
RUN pipenv install --system


# Copy project
COPY . /code/
