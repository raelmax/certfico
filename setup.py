from setuptools import setup

setup(
    name='certifico',
    version='0.0.1',
    packages=['certifico'],
    include_package_data=True,
    install_requires=[
        'flask',
        'Flask-PyMongo',
        'sendgrid',
        'rq',
        'gunicorn'
    ],
    entry_points = {
        'console_scripts': ['mail-worker=certifico.worker:main'],
    }
)

