# Base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the poetry files and lock file
COPY pyproject.toml poetry.lock /app/

# Install Poetry
RUN pip install poetry

# Copy the rest of the application code
COPY . /app

# Set the working directory to the source code folder
WORKDIR /app/src

# Install project dependencies
RUN poetry install --no-dev

# Set the APP_PORT environment variable
ARG APP_PORT
ENV APP_PORT=${APP_PORT}

# Set the APP_HOST environment variable
ARG APP_HOST
ENV APP_HOST=${APP_HOST}

# Expose the Flask app port
EXPOSE ${APP_PORT}

# Set the entrypoint command
CMD ["poetry", "run", "flask", "run", "--host=$APP_HOST"]
