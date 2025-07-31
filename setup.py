from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="brasil-utils-samuellcs",
    version="0.0.1",
    author="Samuel Lucas",
    author_email="samuellcs@example.com",
    description="Utilitários Python para desenvolvedores brasileiros",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/samuellcs/simple-package-template",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)