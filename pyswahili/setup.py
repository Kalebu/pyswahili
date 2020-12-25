from setuptools import setup, find_packages


setup(
    name='pyswahili',
    version='0.0.1',
    description='''
    Python package for briding python english keywords 
    with swahili one to allow swahili speakers to learn the basics of coding 
    without ever knowing  english 
    '''
    ,
    url='https://github.com/Kalebu/pyswahili',
    author="Jordan Kalebu",
    author_email="isaackeinstein@gmail.com",
    license="MIT",
    package = ['PySwahili'],
    include_package_data=True,
    package_data = {'Swahili': ['sw_to_english.json', '*.py']},
    install_requires=[
        'click',
    ],
    
    entry_points='''
        [console_scripts]
        pyswahili=Swahili.cli:cli
        ''', 
)
