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

Crie a sua imagem do container docker

```bash
  docker build -t nomedasuaimagem .
```

Execute seu container utilizando a flag -p (representa a porta que irá executar o servidor)

```bash
  docker run -p 8000:8000 nomedasuaimagem
```

