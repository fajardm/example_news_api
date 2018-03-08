import unittest

from apps import create_app, run
from flask.cli import FlaskGroup

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command()
def start():
    run()


@cli.command()
def test():
    """ Runs the tests without code coverage"""
    tests = unittest.TestLoader().discover('../tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    cli()
