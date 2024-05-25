FROM python:3.10-bullseye

# possible to change python version, see: https://hub.docker.com/_/python/tags

# Set environment varibles+
# PYTHONDONTWRITEBYTECODE - prevents Python from writing these .pyc files.
# PYTHONUNBUFFERED - Python's stdout and stderr streams are unbuffered, so live visible in container
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install build and python dependencies (needed for poetry installation)
RUN apt-get update && \
    apt-get -y install gcc libc-dev curl libffi-dev musl-dev openssl gcc python3-dev cargo

# Install Poetry (see latest: https://pypi.org/project/poetry/) and add to path
RUN curl -sSL https://install.python-poetry.org | python3 -
# ENV POETRY_VERSION=1.5.1
# RUN curl -sSL https://install.python-poetry.org | POETRY_VERSION=$POETRY_VERSION python3 -
# RUN curl -sSL https://install.python-poetry.org | python3 - --git https://github.com/python-poetry/poetry.git@master
ENV PATH="/root/.local/bin:$PATH"

# Copy source code (see .dockerignore)
COPY . /app/

# Install project dependencies
COPY poetry.lock pyproject.toml /app/
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi


# Install Gunicorn, a webserver for flask (https://gunicorn.org/)
RUN pip install gunicorn

# (optional) remove build dependencies to save space
# RUN apk del .tmp

EXPOSE 8000

# Create and use a non-root user
RUN groupadd -r rquser && useradd -m -r -g rquser rquser
RUN mkdir -p /app/logs && chown -R rquser:rquser /app/logs
USER rquser

# Set the command to run your application. gunicorn is a WSGI HTTP server for Python web applications.
# 0.0.0.0 -> means it will listen to all IPv4 addresses, including localhost on the host machine. 
# Setting here 127.0.0.1 would mean only accessible to container itself, which makes no sense since we want to access from outside of container.
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "ethberlin_schufher_flask.app:app"]

# run this image: docker run -p 8000:8000 <image-name>