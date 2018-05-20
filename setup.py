import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name='haburas',
    description='make app for hadezta',
    version='0.1.1',
    author='Mariano de Deus',
    author_email='anau456anu@gmail.com',
    license='MIT',
    url='https://github.com/eraulo/Setup_haburas',
    long_description=open('README.rst').read(),
    packages=[
        'haburas',
    ],
    install_requires=[
        'Django>=2.0.3',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ]
)
