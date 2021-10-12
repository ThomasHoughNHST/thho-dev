FROM python:3.7

WORKDIR /app

COPY . /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]