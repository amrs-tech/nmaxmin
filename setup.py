import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nmaxmin",
    version="1.0.1",
    author="Ahamed Musthafa",
    author_email="amrs.tech@gmail.com",
    description="A package to find nth max and min in a given list",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amrs-tech/nmaxmin",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
)