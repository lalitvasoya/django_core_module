import setuptools

REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]

with open("README.rst", "r") as readme_file:
    long_description = readme_file.read()

setuptools.setup(
    name="core",
    version="1.0.0",
    author="Tntra",
    author_email="tntra@tntra.io",
    description="Core module for shairu contains the models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    project_urls={
        "Bug Tracker": "",
    },
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    install_requires=REQUIREMENTS,
    python_requires=">=3.9",
)
