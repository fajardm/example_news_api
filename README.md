# Table of Contents
1. [Demo](#demo)
2. [Dockerized](#dockerized)
3. [Generate Apidoc](generate-apidoc)

## Demo
Comming soon

## Dockerized
1. Configuration
Copy paste `config.cfg.example` to ` config.cfg` and change variable in the file based on your environment

2. Docker Compose

```
docker-compose up --build -d
```

## Apidoc
1. Install `npm install apidoc -g`
2. Run `apidoc -i apps/ -o apidoc/ -f ".*\\.py$"` inside this project.
3. Find and open `index.html` inside `apidoc` directory
4. You can read full documentation here `http://apidocjs.com/`
