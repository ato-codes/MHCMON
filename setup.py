from setuptools import setup
setup(
    name="MHCMON",
    version="0.0.1",
    description="Simple Auto C# And Bash Script Runner On Save",
    author="ato-codes MHCDA",
    author_email="thecmboy930@gmail.com",
    entry_points={
        'console_scripts':[
            'mhcmon=mhcmon'
        ]
    }
)