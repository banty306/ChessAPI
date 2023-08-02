FROM python:3.10.4

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE='chessApp/settings'

# Set the timezone to Asia/Kolkata
ENV TZ="Asia/Kolkata"

# Install required system dependencies and GDAL
RUN apt-get update && \
    apt-get install -y gdal-bin && \
    apt-get clean

# Set the working directory in the container
WORKDIR /ChessAPI

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port that Django's development server runs on (if applicable)
EXPOSE 8000

# Start the Django development server when the container is run
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--settings=chessApp.settings"]
