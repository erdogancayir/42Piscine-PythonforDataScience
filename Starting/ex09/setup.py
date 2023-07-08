# setup.py
from setuptools import setup, find_packages

setup(
    name='ft_package',
    version='0.0.1',
    url='https://github.com/eagle/ft_package',
    author='Eagle',
    author_email='eagle@42.fr',
    description='A sample test package',
    packages=find_packages(),    
    install_requires=[],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
