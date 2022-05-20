from setuptools import setup, find_packages

with open('LICENSE') as f:
    license = f.read()

with open("requirements.txt") as f:
    requireds = f.read().splitlines()

setup(
    name='eth_utils',
    version='0.1.0',
    description='Some ETH utils',
    long_description="A longer description of some ETH utils",
    author='JJ',
    author_email='',
    url='https://github.com/jj-btc/unamed-utils.git',
    install_requires=requireds,
    license=license,
    packages=find_packages(exclude=('tests', 'docs', 'examples'))
)