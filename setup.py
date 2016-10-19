from setuptools import setup, find_packages


classifiers = [
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
    'Topic :: Software Development :: Libraries',
    'Intended Audience :: Developers',
    'Framework :: Django',
]

with open("README.rst") as f:
    long_description = f.read()

setup(
    name='djangorestframework-queryfields',
    version='1.0.0',
    description='Serialize a partial subset of fields in the API',
    long_description=long_description,
    packages=find_packages(exclude=['tests']),
    author='Wim Glenn',
    author_email='hey@wimglenn.com',
    url='https://github.com/wimglenn/djangorestframework-queryfields',
    classifiers=classifiers,
    extras_require={
        'dev': ['setuptools', 'wheel', 'pytest-django', 'djangorestframework', 'django', 'mock_django']
    },
)
