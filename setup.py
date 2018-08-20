import setuptools 

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(name='table describer',
      version='0.1.4.1',
      description='Quickly get characterstics of a delimited table',
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
		install_requires=[],
      zip_safe=False)
