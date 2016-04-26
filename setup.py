from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()


setup(
    name='app',
    version='1.0.0',
    description='Python boilerplate application',
    long_description=readme,
    author='Roberto Paredes',
    author_email='rdparedessalazar@gmail.com',
    url='https://github.com/rdparedes/python-boilerplate',
    license='MIT',
    packages=find_packages(exclude=('tests', 'docs'))
)