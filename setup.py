#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = [
    "importlib-resources",
    "validators",
    "requests",
    "marshmallow_dataclass",
    "kivy",
    "kivymd",
]

test_requirements = [
    "pytest>=3",
]

setup(
    author="Jerrad Anderson",
    author_email="jayrod84@gmail.com",
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Inventory client for Urban Girl Yarns Web api",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="ugy_inventory_client",
    name="ugy_inventory_client",
    packages=find_packages(include=["ugy_inventory_client", "ugy_inventory_client.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/jayrod/ugy_inventory_client",
    version="0.1.0",
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "ugy = ugy_inventory_client.ui.main:main",
        ],
    },
)
