""" A setuptools bale setup module
"""

from os import path
from setuptools import setup
from setuptools import find_namespace_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf8') as readme:
    long_description = readme.read()

setup(
    name='inputting',
    version='0.0.1',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='ankiav',
    author_email='anklavvanlove@gmail.com',
    url='https://github.com/ankIav/Katser_TeachMeSkills_Homeworks/tree/main/HW_15/package',
    download_url='',
    license='LICENSE',
    keywords=['input', 'inputting', 'int', 'float'],
    package_dir={'': 'inputting'},
    packages=find_namespace_packages(where='inputting'),
    python_requires='>= 3.6, <4',
)
