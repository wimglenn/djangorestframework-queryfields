from setuptools import setup


classifiers = [
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Topic :: Software Development :: Libraries',
    'Intended Audience :: Developers',
    'Framework :: Django',
]

with open("README.rst") as f:
    long_description = f.read()

setup(
    name='djangorestframework-queryfields',
    version='1.1.0',
    description='Serialize a partial subset of fields in the API',
    long_description=long_description,
    packages=['drf_queryfields'],
    author='Wim Glenn',
    author_email='hey@wimglenn.com',
    license='MIT',
    url='https://github.com/wimglenn/djangorestframework-queryfields',
    classifiers=classifiers,
    extras_require={
        'dev': [
            'pytest', 'pytest-cov', 'pytest-django', 'coveralls',
            'django', 'djangorestframework', 'mock_django',
            'setuptools', 'wheel', 'pytz',
        ]
    },
)
