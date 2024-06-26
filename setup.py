import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="openvector",
    version="0.0.3",
    author="Eddy Jin",
    description="An open source vector database.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eddyjin1/openvector",
    packages=setuptools.find_packages(),
    install_requires = [],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
