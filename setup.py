import setuptools 

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(name='table describer',
            version='0.1.6',
            description='Quickly get characteristics of a delimited table',
            long_description=long_description,
            long_description_content_type="text/markdown",
            url='https://github.com/ryansutc/table_describer',
            author='Ryan Sutclif',
            author_email="ryansutc@gmail.com",
            license='GNU',
            packages=setuptools.find_packages(),
            classifiers=[
                "Programming Language :: Python :: 2",
                "License :: OSI Approved :: MIT License",
                "Operating System :: OS Independent",
            ],
            entry_points={
                  'console_scripts': ['tbl_desc=table_describer.__init__.py:main'],
            },
            install_requires=['pandas<0.23.1'],
            extras_require={'dev': ["jupyter", "pytest"]},
            zip_safe=False)
