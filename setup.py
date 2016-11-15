from setuptools import setup

setup(
        name='py488',
        version='1.0',
        packages=['py488'],
        install_requires=['pyusb'],
        author='Fredrik Ahlberg',
        author_email='fredrik@z80.se',
        description='Python library for communicating with Ful488',
        license='GPL2',
)
