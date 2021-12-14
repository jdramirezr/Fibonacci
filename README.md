# Fibonnaci

Running with Docker

```bash
  docker build -t hey .
  docker run -p 8000:8000 hey

```

Running without Docker

```bash
  python3 -m virtualenv venv
  source venv/bin/activate
  pip3 install -r requirements.txt
  python manage.py runserver
```

  http://0.0.0.0:8000/api/fibonacci/
