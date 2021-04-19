from setuptools import setup

setup(
    name="pyswahili",
    version="0.1.0",
    packages=["pyswahili"],
    entry_points={
        "console_scripts": [
            "pyswahili = pyswahili.__main__:main"
        ]
    },
)
