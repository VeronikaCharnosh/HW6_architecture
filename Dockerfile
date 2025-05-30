FROM python:3.11-slim

WORKDIR /app

ARG SERVICE
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ${SERVICE}/${SERVICE}.py app.py

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
