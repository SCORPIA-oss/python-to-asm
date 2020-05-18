import setuptools

with open("py2asm/README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="py2asm",
	version="0.0.1",
	
	
	author="py2asm group",
	author_email="xsumagravity@gmail.com",
	
	
	description="A package for converting python to asm compiled code",
	
	
	long_description=long_description,
	long_description_content_type="text/markdown",
	
	
	url="https://github.com/pypa/sampleproject",
	packages=setuptools.find_packages(),
	
	
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: MacOS",
	],
	python_requires='>=3.6',
)
