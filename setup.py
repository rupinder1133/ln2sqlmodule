from distutils.core import setup
setup(
    name = 'ln2sqlmodule',
    packages = ['ln2sqlmodule'],
    version = '0.0.1',
    license='gpl-3.0',
    description = 'This is a wrapper around ln2sql by Jérémy Ferrero for convenient use',
    author = 'Rupinder Singh',
    author_email = 'rupinder1133@gmail.com',
    url = 'https://github.com/rupinder1133',
    download_url = 'https://github.com/rupinder1133/ln2sqlmodule',    # I explain this later on
    keywords = ['ln2sql', 'NLP', 'SQL'],
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU General Public License v3.0',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2',
    ],
)
