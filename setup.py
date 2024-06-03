from setuptools import setup, find_packages

setup(
    name='tarp',
    version='0.1.1',
    author='Pablo Lemos',
    url='https://github.com/Ciela-Institute/tarp',
    install_requires=[
        'numpy',
        'scipy',
        'deprecation',
    ],
    packages=find_packages(where='src', include=['tarp'], exclude=['tarppp']),
    package_dir={'': 'src'},
)
