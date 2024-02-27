FROM python:3.9

COPY . /app
COPY app.py .
COPY templates .
COPY trabalho1clienteservidor.sql .

RUN pip install --no-cache-dir flask mysql-connector-python

WORKDIR /app

EXPOSE 3306
CMD ["python", "app.py"]
