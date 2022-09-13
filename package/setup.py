import setuptools
from setuptools import setup, find_packages
from sheriff import __version__

VERSION = __version__

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
    install_requires=['colorama','dlib','numpy','opencv_python','Pillow','PyQt5','PySide6','regex'],
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