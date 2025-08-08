from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as req_file:
    requirements = req_file.read().splitlines()

setup(
    name="primeiro_pacote",
    version="0.1.0",
    author="Rafael Cremasco Lacerda",
    description="Meu primeiro pacote Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rafaelcremasco2/trilha-python-dio/tree/main/06%20-%20Gerenciamento%20de%20pacotes%20e%20boas%20pr%C3%A1ticas/desafio",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.6",
)