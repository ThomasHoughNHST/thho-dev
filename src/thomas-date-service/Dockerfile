<<<<<<< HEAD
FROM python:3.7

WORKDIR /app

COPY . /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
=======
FROM python:3.8-slim-buster
WORKDIR /usr/src/app
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
#Server will reload itself on file changes if in dev mode
ENV FLASK_ENV=development
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["flask", "run"]
>>>>>>> 99af73d9b28d413d4c3e911189f1860f9d30d995
