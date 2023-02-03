FROM python:3.9

ENV PYHTHONBUFFERED=1

WORKDIR /djangoapp

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python","manage.py","runserver"]