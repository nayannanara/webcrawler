# WebCrawler

Este projeto fará um web crawler nos sites da Digital Ocean e Vultr, com o objetivo de extrair algumas informações, realizando o web scraping.

As informações coletadas de cada site são: 
`cpu_vcpus, memory, storage_ssd_disk, bandwith_transfer, price_by_month`.

Para executar o projeto, utilizei a [pyenv](https://github.com/pyenv/pyenv), com a versão 3.10.0 do `python` para o ambiente virtual.

Caso opte por usar pyenv, execute:

```bash
pyenv virtualenv 3.10.0 crawler
pyenv activate crawler
```
Eu utilizei o `argparse` para trazer um "menu" de opções. Portanto, para rodar o projeto e verificar quais ações possui, execute:

```bash
python run.py -h
```
As opções exibidas são estas:
```bash
usage: run.py [-h] --site SITE --output OUTPUT

options:
  -h, --help       show this help message and exit
  --site SITE      [vultr/digitalocean]
  --output OUTPUT  [cmd/csv/json]
```
Para o argumento `--site` passe `vultr ou digitalocean` e `output` passe `cmd/csv/json`.

Por exempĺo:
```bash
python run.py --site digitalocean --output csv
```

Os dados podem ser exibidos de três formas: pelo terminal, csv e json. Ao optar por csv e json, é criada uma pasta no diretório `files/` com os devidos arquivos.