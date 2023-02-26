# API Farms - Django Rest

Este repósitorio tem o objetivo de apresentar este projeto.

## Como rodar na sua máquina

Clone o projeto

```bash
  git clone git@github.com:juliocesar014/farm_project.git
```

Entre no diretório do projeto

```bash
  cd farm_project
```

Entre no backend do projeto

```bash
  cd backend
```

Crie um ambiente virtual

```bash
  python -m venv .venv
```

Ative o ambiente virtual

```bash
.venv\Scripts\activate
```

Instale as dependências

```bash
  pip install -r requirements.txt
```

Crie um superuser

```bash
python manage.py createsuperuser
```

Inicie o servidor

```bash
  python manage.py runserver
```

## Página Inicial da API

![Screen](https://uploaddeimagens.com.br/images/004/366/633/original/api-init.png?1677261399)

## Página Lista Farms API

![Scren](https://uploaddeimagens.com.br/images/004/366/638/original/farm-api.png?1677261579)

## Página Lista Owners API

![Screen](https://uploaddeimagens.com.br/images/004/366/642/original/owners-api.png?1677261658)

## Funcionalidades

- Consultar/Criar/Atualizar/Deletar lista de Fazendas
- Consultar/Criar/Atualizar/Deletar lista de Proprietários
