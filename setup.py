from setuptools import setup

setup(
    name="pyswahili",
    version="0.1.0",
    description="""
    Python package for briding python english keywords 
    with swahili one to allow swahili speakers to learn the basics of coding 
    without ever knowing  english 
    """,
    url="https://github.com/Kalebu/pyswahili",
    author="Jordan Kalebu",
    author_email="isaackeinstein@gmail.com",
    license="MIT",
    packages=["pyswahili"],
    entry_points={
        "console_scripts": [
            "pyswahili = pyswahili.__main__:main"
        ]
    },
)
