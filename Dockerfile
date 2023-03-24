# FROM python:3.9
# WORKDIR /apps
# COPY requirements.txt .
# RUN pip install -r requirements.txt
# COPY manage.py .
# COPY ws2/ ws2/
# COPY app1/ app1/
# copy templates/ templates/
# copy . /webscrape_oracle
# EXPOSE 8000
# CMD ["python3", "manage.py", "runserver"]



FROM python:3.9

WORKDIR /app1

COPY requirements.txt requirements.txt

RUN pip3 install --no-cache-dir -r requirements.txt

RUN pip install djongo

COPY . .

EXPOSE 8000

CMD ["python3", "manage.py", "runserver"]

#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myapp.wsgi:application"]

