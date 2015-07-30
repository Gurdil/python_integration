Python Integration
========================================================

Example of tool used :

* Epydoc for doc
* Pytest for test
* Pypi for distribution

Pypi server:
------------
see: https://pypi.python.org/pypi/pypiserver

You need to create a .htaccess to store the user/password information at the root of the server.

    htpasswd -sc .htaccess <some_username>

You start the server with :
    
    ./pypi-server -p 8080 -P .htaccess ~/packages &

On client side create a ~/.pypirc to strore you're account:
    
    [distutils]
    index-servers =
      pypi
      internal
    
    [pypi]
    username:<your_pypi_username>
    password:<your_pypi_passwd>
    
    [internal]
    repository: http://localhost:8080
    username: <some_username>
    password: <some_passwd>

Then you can push your lib:
    
    python setup.py sdist upload -r internal

You can install it with pip:
--------------------------

    pip install --extra-index-url http://localhost:8080/ python_integration

or upgrade with:
    
    pip install --extra-index-url http://localhost:8080/ python_integration --upgrade

Exemple of use:
--------------------------

Direct with line command :

    $ python_integration

In python:
    
    >>> from python_integration import show
    >>> show()

util :
---------

Delete all pyc file :
    
     find . -name '*.pyc' -delete

virtual environment with pycharm :
--------------

create a virtual environment :

* --no-site-packages to a empty virtual environment
* -p path/to/python/to/use the python used in the virtual environment 


    virtualenv /path/to/your/projet/{environment_name}

activate a virtual environment :

    source {path to the virtual event}/bin/activate

### pycharm :

create a .pycharmrc file at the root of project:
    
    source ~/.bashrc
    source {path to the virtual event}/bin/activate

Change in : File > Settings... > Tools > Terminal > shell path

    /bin/bash --rcfile ./.pycharmrc


Ce code est sous licence WTFPL.