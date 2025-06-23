"""Setup.py for OpenEA."""

import os

import setuptools

MODULE = 'openea'
VERSION = '1.0'
PACKAGES = setuptools.find_packages(where='src')
META_PATH = os.path.join('src', MODULE, '__init__.py')
KEYWORDS = ['Knowledge Graph', 'Embeddings', 'Entity Alignment']
INSTALL_REQUIRES = [
    # 'tensorflow',
    'pandas==0.24.2',
    'matching==0.1.1',
    # added my own version nums
    'scikit-learn==0.20.0',
    'numpy==1.16.0',
    'gensim==3.7.3',
    'python-Levenshtein',
    'scipy==1.2.1',
    'psutil==5.8.0'
]

if __name__ == '__main__':
    setuptools.setup(
        name=MODULE,
        version=VERSION,
        description='A package for embedding-based entity alignment',
        url='https://github.com/nju-websoft/OpenEA.git',
        author='Zequn Sun',
        author_email='zqsun.nju@gmail.com',
        maintainer='Zequn Sun',
        maintainer_email='zqsun.nju@gmail.com',
        license='MIT',
        keywords=KEYWORDS,
        packages=setuptools.find_packages(where='src'),
        package_dir={'': 'src'},
        include_package_data=True,
        install_requires=INSTALL_REQUIRES,
        zip_safe=False,
    )
