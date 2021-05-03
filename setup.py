from setuptools import setup

setup(
    name='mypackage',
    version='beta1.0.0',
    packages=['cocanb'],
    install_requires=[
        'importlib',
        'numpy',
        'unidecode'
    ],
)