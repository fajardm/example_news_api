from setuptools import setup, find_packages

setup(
    name='app',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'Flask-WTF',
        'pymysql',
        'Flask-SQLAlchemy',
        'Flask-Migrate',
        'flask-marshmallow',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)
