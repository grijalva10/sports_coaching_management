from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in sports_coaching_management/__init__.py
from sports_coaching_management import __version__ as version

setup(
	name="sports_coaching_management",
	version=version,
	description="sports_coaching_management",
	author="JMG",
	author_email="grijalva10@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
