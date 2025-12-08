# Use an official Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the decision table update script
RUN python policy_rules/decision_tables/update_all_decision_tables_script.py

# Set default command (adjust if needed)
CMD ["python", "flow.py"]
