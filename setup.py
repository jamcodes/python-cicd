# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

_script_dir = os.path.realpath(os.path.dirname(__file__))

def get_version_str(version_tuple):
    '''
    Given an iterable of int-like values
    returns a '.' separated version string.
    '''
    return '.'.join(str(x) for x in version_tuple)

def get_version_tuple_fallback(name):
    init_path = os.path.join(name, '__init__.py')
    ver_line = next(filter(lambda l: l.startswith('VERSION'), open(init_path)))
    return get_version_str(eval(ver_line.split('=')[-1]))

try:
    import webcount
    _version = webcount.VERSION
except Exception as ex:
    print(ex)
    _version = get_version_tuple_fallback(os.path.join(_script_dir,'webcount'))

try:
    with open(os.path.join(_script_dir, 'README.md')) as f:
        readme = f.read()
except Exception as e:
    print(e)
    readme = 'python CI/CD sandbox'

setup(
    name='webcount',
    version=get_version_str(_version),
    description='python CI/CD sandbox',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Jeremi Mucha',
    author_email='jam.sfinae@gmail.com',
    url='',
    license='Unlicense',
    install_requires=['requests'],
    packages=find_packages(exclude=('test', 'docs', 'etc', 'bin'))
)
