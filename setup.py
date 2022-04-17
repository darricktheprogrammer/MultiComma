import setuptools

import multicomma

with open("README.md", "r") as readme:
	long_description = readme.read()

setuptools.setup(
	name="MultiComma",
	version=multicomma.__version__,
	url="https://github.com/darricktheprogrammer/multicomma",

	author="Darrick Herwehe",
	author_email="darrick@exitcodeone.com",

	description="Placeholder text for short description",
	long_description=long_description,
	license="MIT",

	packages=setuptools.find_packages(),

	install_requires=[],

	classifiers=[
		"Development Status :: 2 - Pre-Alpha",
		"Programming Language :: Python",
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.9",
	],
)
