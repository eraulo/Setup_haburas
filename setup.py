from setuptools import setup


setup(
    name='haburas',
    description='make app for hadezta',
    version='0.0.1',
    author='Mariano de Deus',
    author_email='anau456anu@gmail.com',
    license='MIT',
    url='https://github.com/eraulo/Setup_haburas/haburas',
    long_description=open('README.rst').read(),
    packages=[
        'haburas',
    install_requires=[
        'Django>=2.0.3',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: System :: Installation/Setup'
    ]
)
