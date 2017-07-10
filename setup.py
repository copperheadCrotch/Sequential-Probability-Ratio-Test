from setuptools import setup, find_packages, Extension
from os import path
import numpy

here = path.abspath(path.dirname(__file__))

install_requires = []

try:

    import matplotlib

except ImportError:

    install_requires.append('matplotlib')

try:

    import numpy

except ImportError:

    install_requires.append('numpy')

try:

    import pandas

except ImportError:

    install_requires.append('append')

setup(
    include_dirs=[numpy.get_include()],
    name='sprt',
    version='0.0.1',
    description='Python package to do sequential probability ratio test',
    url='https://github.com/ContaTP/Sequential-Probability-Ratio-Test',
    author='Zhenning Yu',
    author_email='yuzhenning.bio@gmail.com',
    zip_safe=False,
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
    keywords='sequential analysis, sprt, likelihood, likelihood ratio, Wald',
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=install_requires
)
