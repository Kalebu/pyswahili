from setuptools import setup

setup(
    name="pyswahili",
    version="0.1.2",
    description="""
    Python package for briding python english keywords 
    with swahili one to allow swahili speakers to learn the basics of coding 
    without ever knowing  english 
    """,
    url="https://github.com/Kalebu/pyswahili",
    download_url='https://github.com/Kalebu/pyswahili/releases/tag/0.1',
    author="Jordan Kalebu",
    author_email="isaackeinstein@gmail.com",
    license="MIT",
    packages=["pyswahili"],
    keywords=[
        "pyswahili",
        "python-tanzania",
        "python-transpiler",
        "swahili-python",
        "python in swahili",
        "python for swahili speakers",
        "code python in swahili",
        "swahili programming language",
        "program in swahili",
    ],
    entry_points={
        "console_scripts": [
            "pyswahili = pyswahili.__main__:main"
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ]
)
