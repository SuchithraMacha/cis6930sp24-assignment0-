from setuptools import setup, find_packages

setup(
    name='assignment0',
    version='1.0',
    author='Suchithra Macha',
    author_email='your ufl email',
    packages=find_packages(exclude=('tests', 'docs', 'resources')),
    install_requires=[
        'certifi==2024.2.2',
        'charset-normalizer==3.3.2',
        'idna==3.6',
        'pypdf==4.0.1',
        'requests==2.31.0',
        'urllib3==2.2.0'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)
