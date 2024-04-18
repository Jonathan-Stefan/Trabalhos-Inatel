FROM python:3.9

RUN apt-get update -y 
RUN apt-get install -y python3-pip

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install flask mysql-connector-python

COPY . .

EXPOSE 5000

CMD ["python", "./app.py"]