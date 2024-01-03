from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="kenna",
    version="4.0.0",
    author="Tyler Fisher",
    author_email="tyler.fisher@canadalife.com",
    description="An API client for Kenna Security",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://git.gwl.bz/projects/GSA/repos/kenna-api-client/browse",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Security",
    ],
    packages=find_packages(),
    install_requires=[],
)
