from setuptools import setup, Command, find_packages


# you can also import from setuptools

class PyTest(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import subprocess
        import sys
        errno = subprocess.call([sys.executable, 'runtests.py'])
        raise SystemExit(errno)


class PyDoc(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import subprocess
        import sys
        errno = subprocess.call(['epydoc --config ./epydocConfig.ini'], shell=True)
        raise SystemExit(errno)


import python_integration

setup(
    name='python_integration',
    version=python_integration.__version__,
    packages=find_packages(),
    url='',
    license='WTFPL',
    author='PHILIPPE Jean-Baptiste',
    author_email='jbphilippe@live.fr',
    description='An empty project to test python tool : py.test, epydoc, setup.py...',
    long_description=open('README.md').read(),
    cmdclass={'test': PyTest, 'doc': PyDoc},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'python_integration = python_integration.main:show',
        ],
    },
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 1 - Planning",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.4",
        "Topic :: Test",
    ],
    install_requires=open('requirements.txt', 'r').read().splitlines()
)
