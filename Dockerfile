FROM python:3.6

ADD . /app
WORKDIR /app

RUN pip install -r requirements.txt

# Uncomment this for develop
EXPOSE 3000

CMD ["python", "run.py"]

# Uncomment this for heroku
# Run the app.  CMD is required to run on Heroku
# $PORT is set by Heroku
#CMD gunicorn --bind 0.0.0.0:$PORT wsgi