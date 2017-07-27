from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

setup(
    name='cloud_creator',
    version='0.1.0',
    description='Python module for importing cloudFormation template, validating and creating a cloudFormation stack.',
    long_description=readme,
    author='Quadyster_dev_team',
    author_email='nvallepalli@quadyster.com',
    url='https://github.com/nvallepalli/cloud_creator.git',
    packages=find_packages(exclude=('tests', 'docs'))
)