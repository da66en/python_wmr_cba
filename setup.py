import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wmr_cba",
    version="1.1.0",
    author="Darren Rook (da66en)",
    author_email="route66@gmail.com",
    description="Python module for controlling West Mountain Radio CBA devices.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/da66en/python_wmr_cba",
    install_requires=[
        'pyusb'
    ],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)