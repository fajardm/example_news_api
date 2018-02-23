# Table of Contents
1. [Demo](#demo)
2. [How to](#how-to)
3. [Dockerized](#dockerized)
4. [Migration](#migration)
5. [Generate Apidoc](generate-apidoc)

## Demo
1. API `https://example-news-api.herokuapp.com/ping`
2. API DOC `https://example-news-api-doc.herokuapp.com/`

## How to
1. You must change the following files based on your environment. Specific needs if deployed in Heroku. 
`apidoc/default.conf.template`
`apidoc/Dockerfile`
`Dockerfile`
`config.cfg.example`
2. Run apidoc
3. Run dockerized
4. Run migration
5. API host `http://localhost:3000`
6. Apidoc host `http://localhost:4000`

## Dockerized
1. Configuration

Copy paste `config.cfg.example` to ` config.cfg` and change variable in the file based on your environment

2. Docker Compose

```
docker-compose up --build -d
```

## Migration
**Migration in docker**
1. Run `sudo docker-compose run --rm api bash`. `api` is the name of service at docker-compose file
2. Enter `export FLASK_APP=run.py`
3. Enter `flask db upgrade`

**Migration in development**
1. Enter `export FLASK_APP=run.py`
2. Run `flask db init` for first time
3. Run `flask db migrate` for update schema
4. Run `flask db upgrade` for push to database
5. You can read full documentation here `https://flask-migrate.readthedocs.io/en/latest/` 

## Apidoc
**Generate apidoc**
1. Install `npm install apidoc -g`
2. Run `apidoc -i apps/ -o apidoc/ -f ".*\\.py$"` inside this project.
3. Find and open `index.html` inside `apidoc` directory
4. You can read full documentation here `http://apidocjs.com/`
