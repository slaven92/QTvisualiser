import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="slaven92-QTvisualiser",
    version="1.1.2",
    description="Visualise cross section of a 3D image",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/slaven92/QTvisualiser",
    author="Slaven Tepsic",
    author_email="slaven.tepsic@icfo.eu",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["QTvisualiser"],
    include_package_data=True,
    install_requires=["PyQt5", "pyqtgraph"],
    entry_points={
        "console_scripts": [
            "visualise=QTvisualiser.__main__:main",
        ]
    },
)
