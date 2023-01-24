from setuptools import setup,find_packages

VERSION = '0.0.1'
DESCRIPTION = 'auto run bash and c# scripts on save'
LONG_DESCRIPTION = 'A pyton cli app which auto runs your bash script or c# script.'

setup(
    name="MHCMON",
    version=VERSION,
    author="ato-codes MHCDA",
    author_email="thecmboy930@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    keywords=['bash','c#','python'],
    entry_points={
        'console_scripts':[
            'mhcmon=mhcmon'
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: Debian :: Ubuntu",
        "Operating System : Microsoft :: Windows",
    ]
)