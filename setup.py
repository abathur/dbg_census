from setuptools import setup, find_packages

setup(
    name='dbg_census',
    version='1.0.0',
    author='Travis A. Everett',
    author_email='travis.a.everett@gmail.comm',
    packages=['dbg_census'],
    url='https://github.com/abathur/dbg_census',
    license='LICENSE.md',
    description="Minimalistic Python wrapper for Daybreak Games Census API, which provides stats and other information for DBG titles like Planetside 2, Everquest 2, and DC Universe Online.",
    long_description=open('README.md').read(),
    install_requires=[
        "requests",
    ],
)
