from os import path
from setuptools import setup

with open(path.join(path.dirname(path.abspath(__file__)), 'README.rst')) as f:
    readme = f.read()

setup(
    name             = 'gnuplot',
    version          = '0.1',
    description      = 'An app to ...',
    long_description = readme,
    author           = 'rkpattnaik780',
    author_email     = 'rkpattnaik780@gmail.com',
    url              = 'http://wiki',
    packages         = ['gnuplot'],
    install_requires = ['chrisapp'],
    test_suite       = 'nose.collector',
    tests_require    = ['nose'],
    license          = 'MIT',
    zip_safe         = False,
    python_requires  = '>=3.6',
    entry_points     = {
        'console_scripts': [
            'gnuplot = gnuplot.__main__:main'
            ]
        }
)
