#!/usr/bin/env python

"""The setup script."""

import pathlib

from setuptools import find_packages, setup

requirements = [
    "pandas==1.4.1",
    "numpy==1.20.3",
    "tqdm==4.64.0",
    "boto3==1.23.4",
    "torch==1.11.0",
    "pytorch_lightning==1.9.3",
    "scanpy==1.9.1",
    "anndata==0.8.0",
    "pytorch_tabnet==3.1.1",
    "torchmetrics==0.10.3",
    "scikit-learn==1.0.2",
    "scipy==1.8.0",
    "wandb==0.12.16",
]

setup_requirements = requirements.copy()

test_requirements = []

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    author="Julian Lehrer",
    author_email="jmlehrer@ucsc.edu",
    python_requires=">=3.9",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Scalable, Interpretable Deep Learning for Single-Cell RNA-seq Classification",
    install_requires=requirements.copy(),
    license="MIT license",
    long_description=README,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="scsims",
    name="scsims",
    packages=find_packages(exclude=["tests"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/jlehrer1/sims",
    version="2.0.1",
    zip_safe=False,
)
