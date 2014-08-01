from setuptools import setup, find_packages

setup(
    name='bitcoin-explorer',
    author='bostonlink',
    version='1.0',
    author_email='bostonlink@igetshells.io',
    description='Blockexplorer-monitor searches the bitcoin blockchain and gathers data about a specific bitcoin address.  Further it allows you to search for the bitcoin address on the web to attempt to associate a user/person/persona to a specific bitcoin address.',
    license='GPL',
    packages=find_packages('src'),
    package_dir={ '' : 'src' },
    zip_safe=False,
    package_data={
        '' : [ '*.gif', '*.png', '*.conf', '*.mtz', '*.machine' ] # list of resources
    },
    install_requires=[
        'canari',
        'requests',
        'beautifulsoup4'
    ],
    dependency_links=[
        # custom links for the install_requires
    ]
)
