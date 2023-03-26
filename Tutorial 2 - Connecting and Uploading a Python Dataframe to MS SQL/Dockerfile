# Use the official Python image as the base image
FROM python:3.9

# Install necessary packages
RUN apt-get update && \
    apt-get install -y build-essential apt-utils unixodbc-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install the ODBC driver for SQL Server
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql17 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Copy the application files to the container
WORKDIR /app
COPY . .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Run the Python application
CMD ["python", "main.py"]
