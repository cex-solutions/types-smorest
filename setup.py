"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
Modified by Madoshakalaka@Github (dependency links added)
"""
from os import path

from setuptools import glob
from setuptools import setup

# Always prefer setuptools over distutils

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="types-smorest",
    description="Type Stubs for flask-smorest",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cex-solutions/types-smorest",
    author="Binovate Labs",
    author_email="cex-dev@binovate.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Flask",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Typing :: Stubs Only",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    license="GPLv3",
    keywords="flask flask-smorest smorest stubs",
    package_data={
        "flask_smorest-stubs": [
            item.split("flask_smorest-stubs/")[-1] for item in glob.glob("**/*.pyi", recursive=True)
        ]
        + ["METADATA.toml"]
    },
    packages=["flask_smorest-stubs"],
    python_requires=">=3.7, <4",
    install_requires=[],
    extras_require={
        "dev": [
            "types-flask==1.1.6",
            "marshmallow==3.21.3",
            "apispec==6.6.1",
            "flask==3.0.3",
            "werkzeug==3.0.3",
            "mypy==1.10.1",
            "twine==5.1.1",
        ]
    },
    dependency_links=[],
    project_urls={
        "Bug Reports": "https://github.com/cex-solutions/types-smorest/issues",
        "Source": "https://github.com/cex-solutions/types-smorest",
    },
)
