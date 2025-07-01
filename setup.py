from setuptools import setup, find_packages

setup(
    name="GroceryListBuilder",
    version="0.1",
    packages=find_packages(),  # this finds the 'grocerylistbuilder' package
    install_requires=[
        "pint",  # and any other dependencies you use
    ],
)