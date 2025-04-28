FROM apache/airflow:latest

# Copy requirements file
COPY requirements.txt /tmp/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Copy DAGs and other files
COPY dags /opt/airflow/dags
COPY plugins /opt/airflow/plugins

# Expose port 8080 for the Airflow webserver
EXPOSE 8080

# Set user to airflow
USER airflow

# Start Airflow components
CMD ["airflow", "webserver", "-p", "8484"