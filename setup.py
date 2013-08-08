from setuptools import setup, find_packages

setup(
    name='soe_api',
    version='0.1.0',
    author='Travis A. Everett',
    author_email='travis.a.everett@gmail.comm',
    packages=['soe_stats'],
    url='https://github.com/abathur/soe_api',
    license='LICENSE.md',
    description="Rudimentary Python API package for Sony Online Entertainment (SOE)'s stats/census API, includes Planetside 2 and Everquest 2.",
    long_description=open('README.md').read(),
    install_requires=[
        "requests",
    ],
)
