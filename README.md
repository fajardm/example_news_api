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
1. Run apidoc
2. Run dockerized
3. Run migration
4. API host `http://localhost:3000`
5. Apidoc host `http://localhost:4000`

## Dockerized
1. Configuration

Copy paste `config.cfg.example` to ` config.cfg` and change variable in the file based on your environment

2. Docker Compose

```
DOCKERFILE_API=Dockerfile-dev DOCKERFILE_APIDOC=Dockerfile-dev docker-compose up --build -d
```

* change `DOCKERFILE_API` and `DOCKERFILE_APIDOC` based on your environment
* read more about flask migration [here](https://flask-migrate.readthedocs.io/en/latest/)

## Migration
**Migration in docker**
1. Database init

```
DOCKERFILE_API=Dockerfile-dev DOCKERFILE_APIDOC=Dockerfile-dev docker-compose exec api python ./apps/manage.py db init
```

2. Database migrate

```
DOCKERFILE_API=Dockerfile-dev DOCKERFILE_APIDOC=Dockerfile-dev docker-compose exec api python ./apps/manage.py db migrate
```

3. Database upgrade

```
DOCKERFILE_API=Dockerfile-dev DOCKERFILE_APIDOC=Dockerfile-dev docker-compose exec api python ./apps/manage.py db migrate
```

**Migration in development**
1. Database init

```
python ./scripts/manage.py db init
```

2. Database migrate

```
python ./scripts/manage.py db migrate
```

3. Database upgrade

```
python ./scripts/manage.py db upgrade
```

* You can read full documentation here `https://flask-migrate.readthedocs.io/en/latest/` 

## Apidoc
**Generate apidoc in development**
1. Install `npm install apidoc -g`
2. Run `apidoc -i apps/ -o apidoc/ -f ".*\\.py$"` inside this project.
3. Find and open `index.html` inside `apidoc` directory

* You can read full documentation here `http://apidocjs.com/`
