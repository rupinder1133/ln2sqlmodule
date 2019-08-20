from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(
    name = 'ln2sqlmodule',
    packages = ['ln2sqlmodule'],
    version = 'v1.0.2',
    license='gpl-3.0',
    description = 'This is a wrapper around ln2sql by Jeremy Ferrero for convenient use',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author = 'Rupinder Singh',
    author_email = 'rupinder1133@gmail.com',
    url = 'https://github.com/rupinder1133/ln2sqlmodule',
    download_url = 'https://github.com/rupinder1133/ln2sqlmodule/archive/v1.0.2.tar.gz',
    keywords = ['ln2sql', 'NLP', 'SQL'],
    install_requires=[],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 2',
    ],
    package_data={
        '': ['stopwords/*.txt', 'lang/*.csv', 'thesaurus/*.dat'],
    },
)
