from setuptools import setup, find_packages, Extension
from os import path
import numpy

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    
    include_dirs=[numpy.get_include()],
    name='sprt',
    version='0.0.1',
    description='https://github.com/ContaTP/Sequentially-Probability-Ratio-Test',
    long_description=long_description,
    url='https://github.com/ContaTP/Sequentially-Probability-Ratio-Test',
    author='Zhenning Yu',
    author_email='yuzhenning.bio@gmail.com',
    zip_safe = False,
    license='GPLv3',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Healthcare Industry',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
    ],
    keywords='sequential analysis, sprt, likelihood',
    packages=find_packages(),
    package_data={'sprt': ['../README.md']},
    install_requires=[
        'numpy',
        'matplotlib'
    ],
)
