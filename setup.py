#!/usr/bin/env python
from distutils.core import setup

setup(name='fv-sectools',
      description='A set of IP-based security checks for websites and applications',
      long_description=open('README.rst').read(),
      version='0.1dev',
      author='F Vicaria',
      author_email='fvicaria@hotmail.com',
      url='http://www.vicaria.org/',
      packages=['fv-sectools', ],
	  python_requires='>=3.6',
      license='MIT License',
      platforms=['Windows']
      )
