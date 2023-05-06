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
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Expose the Flask app port
ARG APP_PORT
ENV FLASK_RUN_PORT=${APP_PORT}
EXPOSE ${APP_PORT}

# Set the entrypoint command
CMD ["poetry", "run", "flask", "run", "--host=0.0.0.0"]
