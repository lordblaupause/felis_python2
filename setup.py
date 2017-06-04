from setuptools import setup, find_packages
import subprocess

with open('VERSION.txt') as fs:
    VERSION = fs.read().strip()

with open('requirements.txt') as fs:
    REQUIREMENTS = fs.read().strip().split('\n')

# compile the rst Version of README.md. rst used on PyPI, md on Github
try:
    out = subprocess.call(['pandoc', '--from=markdown', '--to=rst', '--output=README.rst', 'README.md'])
    if out > 0:
        raise FileNotFoundError
    readme_path = 'README.rst'
except FileNotFoundError:
    print('pandoc not found, using Markdown for README.')
    readme_path = 'README.md'


def readme():
    with open(readme_path) as fs:
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