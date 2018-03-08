from apps.factory import create_app

app = create_app()


def run():
    app.run(host=app.config['APP_HOST'], port=app.config['APP_PORT'])


if __name__ == '__main__':
    run()
