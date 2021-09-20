FROM python:3.7

WORKDIR /app

COPY . /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ENV PORT=8080

EXPOSE 8080

CMD python main.py