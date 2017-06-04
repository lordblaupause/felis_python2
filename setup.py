from setuptools import setup, find_packages
import subprocess

with open('VERSION.txt') as fs:
    VERSION = fs.read().strip()

with open('requirements.txt') as fs:
    REQUIREMENTS = fs.read().strip().split('\n')


def readme():
    with open('README.rst') as fs:
        return fs.read()

setup(name='felis_python2',
      version=VERSION,
      long_description=readme(),
      description='Lecture notes for Python 2 at University of Freiburg.',
      author='Mirko Mälicke',
      author_email='mirko.maelicke@felis.uni-freiburg.de',
      license='MIT',
      packages=find_packages(),
      install_requires=REQUIREMENTS,
      include_package_data=True,
      zip_safe=False

)