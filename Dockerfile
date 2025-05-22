FROM python:3.9-slim
WORKDIR /app
COPY . .  # Copies ALL files (including static/)
RUN pip install flask
CMD ["python", "app.py"]