
from setuptools import setup, find_packages

with open('README.rst') as f:
	readme = f.read()

with open('LICENSE') as f:
	license = f.read()

setup(
	name='logscan',
	version='0.0.1',
	description='Scan log files to run analytics',
	long_description=readme,
	author='Thomas Morreale',
	author_email='ThomasMorreale@gmail.com',
	url='https://github.com/tommrle',
	license=license,
	packages=find_packages(exclude=('tests','docs'))
)
