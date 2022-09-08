import setuptools
from setuptools import setup, find_packages

VERSION = '1.1'

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sheriff",
    version=VERSION,
    author="Gautam Gambhir",
    author_email="ggambhir1919@gmail.com",
    description="An AI enabled program to detect car speed",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Programming-Hero-1313/Sheriff",
    project_urls={
        "Bug Tracker": "https://github.com/Programming-Hero-1313/Sheriff/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    package_dir={'':"src"},
    packages=find_packages('src'),
    python_requires=">=3.10",
    keywords=['speed detector', 'sheriff', 'ai', 'opencv'],
    include_package_data=True
)