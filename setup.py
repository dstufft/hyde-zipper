from setuptools import setup, find_packages

setup(name='hyde-zipper',
version='0.0.3',
description='gzip precompression as post processor',
long_description=open('README.rst').read(),
author='Donald von Stufft',
author_email='donald.stufft@gmail.com',
url='http://github.com/dstufft/hyde-zipper',
classifiers=[
  "Programming Language :: Python",
  "Development Status :: 4 - Beta",
  "Intended Audience :: Developers",
],
keywords='hyde html compressor',
zip_safe=False,
license='BSD',
install_requires=[
'setuptools',
],
packages = find_packages(),
include_package_data = True,
)
