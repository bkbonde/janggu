#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""Setup script"""

from __future__ import absolute_import
from __future__ import print_function

import io
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


def _read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


setup(
    name='janggu',
    version='0.9.5',
    license='GPL-3.0',
    description='Utilities and datasets for deep learning in genomics',
    long_description='%s\n%s' % (
        re.compile('^.. start-badges.*^.. end-badges',
                   re.M | re.S).sub('', _read('README.rst')),
        re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', _read('CHANGELOG.rst'))
    ),
    author='Wolfgang Kopp',
    author_email='wolfgang.kopp@mdc-berlin.de',
    url='https://github.com/BIMSBbioinfo/janggu',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    package_data={'janggu': ['resources/*.fa',
                             'resources/*.bed',
                             'resources/*.csv']},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Utilities',
    ],
    keywords=[
        'genomics', 'epigenomics', 'bioinformatics',
        'deep learning', 'machine learning'
    ],
    install_requires=[
        'numpy',
        'pandas',
        'Biopython',
        'keras==2.1.5',
        'h5py',
        'pybedtools',
        'pydot',
        'pysam',
        'pyBigWig',
        'progress',
        'urllib3',
        'matplotlib',
        'seaborn',
        'scikit-learn',
        'dash',
        'dash_renderer',
        'dash_core_components',
        'dash_html_components'
    ],
    extras_require={
        "tf": ['tensorflow'],
        "tf_gpu": ['tensorflow-gpu']
    },
    entry_points={
        'console_scripts': [
            'janggu = janggu.cli:main',
            'janggu-trim = janggu.janggutrim:main',
        ]
    }
)
