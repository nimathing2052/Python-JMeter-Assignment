from setuptools import setup, find_packages

with open('requrements.txt') as f:
    required = f.read().splitlines()


setup(
    name='datQA',
    version='5.0.0',
    description='solution to assignments given for QA',
    author='Nima Thing',
    author_email='nimathing2052@gmail.com',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=required,
    python_requires='>=3.8',
)