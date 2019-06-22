import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="monitor_example",
    version="0.1",
    author="Aleksandra Kuznetsova",
    author_email="aleksandra_kuznetsova@epam.com",
    description="A small monitor to make snapshots",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
