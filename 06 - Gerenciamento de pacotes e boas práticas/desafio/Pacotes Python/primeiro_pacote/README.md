# Primeiro Pacote Python

Este projeto é um exemplo de pacote Python criado para fins de teste e aprendizado sobre o processo de empacotamento e distribuição de bibliotecas Python. O objetivo é demonstrar como criar, empacotar e publicar um pacote utilizando as ferramentas `setup.py`, `wheel`, `sdist` e `twine`.

## Funcionalidades

- Estrutura básica de um pacote Python
- Configuração de empacotamento com `setup.py`
- Geração de distribuições com `wheel` e `sdist`
- Publicação do pacote no PyPI usando `twine`

## Como usar

1. Instale as dependências necessárias:
    ```bash
    pip install wheel twine
    ```
2. Gere os arquivos de distribuição:
    ```bash
    python setup.py sdist bdist_wheel
    ```
3. Publique o pacote:
    ```bash
    twine upload dist/*
    ```

## Objetivo

Este pacote serve apenas para fins educacionais e de teste, não possuindo funcionalidades específicas além de exemplificar o processo de criação e publicação de pacotes Python.