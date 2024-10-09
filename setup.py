from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Meu_Primeiro_Pacote",
    version="0.0.1",
    author="Thiago_Teiji",
    author_email="thiagotsato@gmail.com",
    description="Meu primeiro pacote para o desafio proposto pela DIO",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ttsvr/simple-package-template"
    packages=find_packages(),
    install_requires=requirements,
)
