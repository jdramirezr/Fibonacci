FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir /app

WORKDIR /app/hey

COPY requirements.txt /app/hey

RUN pip install -r requirements.txt

COPY . /app/hey

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]