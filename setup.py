import setuptools

def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    with open(filename, 'r') as f:
        lineiter = list(line.strip() for line in f)
    return [line for line in lineiter if line and not line.startswith("#")]


install_reqs = parse_requirements("requirements.txt")

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.md') as f:
    readme = f.read()

setup(
  name = 'stylomepy',
  data_files = [("", ["LICENSE.txt", "requirements.txt"], )],
  install_requires=install_reqs,
  packages=setuptools.find_packages(),
  include_package_data=True,
  version = '0.13.1',
  description = 'A Python library for measuring the style.',
  long_description='Stylomepy is a library that allows you to measure the style of Spanish and English texts.',
  author = 'Álvaro de Pablo',
  author_email = 'alvarodepablomarsal@gmail.com',
  url = 'https://github.com/alvarodepablo/stylomepy',
  keywords = ['style', 'measure', 'vocabulary', 'coherence', 'formality', 'readability', 'text'],
  classifiers = [
  'Development Status :: 3 - Alpha',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3',
  ],
  python_requires='>=3',
  )