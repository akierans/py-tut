try:
	from setuptools import setuptools
except ImportError:
	from distutils.core import setuptools

config = {
	'description': 'My Project',
	'author': 'Ash Kierans',
	'url': 'https://github.com/akierans/py-tut'
	'download_url': 'https://github.com/akierans/py-tut'
	'author_email': 'akierans@gmail.com'
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'projectname'
}

setup(**config)