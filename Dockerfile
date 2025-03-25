FROM python:3.12

WORKDIR /app
COPY . /app

RUN pip install requirements
RUN requirements install 

CMD ["requirements", "run", "gunicorn", "app:app"]
