# # FROM alpine:3.18.2
FROM python:3.9.17-slim-bullseye

# RUN pip install --upgrade pip
# # RUN apk update
# # RUN add postgresql-dev gcc python3-dev musl-dev


# WORKDIR /app

COPY requirements.txt requirements.txt
# # WORKDIR app/CRUDEMPLOYEEAPP/

RUN pip install -r requirements.txt

COPY . Blog
# # CMD cd /app/CRUDEMPLOYEEAPP/
WORKDIR /Blog
EXPOSE 8000

 CMD ["python3", "./manage.py","runserver","0.0.0.0:8000"]