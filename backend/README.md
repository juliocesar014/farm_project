# Classe Fazenda (Farm):

name ** obrigatorio
geometry
area
centroid
creation_date
last_modification
is_active
municipio\* ** obrigatorio
estado\* ** obrigatorio
(owner_id)** \*\* obrigatorio

-> Uma fazenda precisa ter obrigatoriamente apenas 1 proprietario e nao pode criar sem proprietario
-> Não pode criar fazendo sem owner,sem municipio, sem estado e sem nome

# Classe Proprietário (Owner):

name ok
document ok
document_type (cpf ou cnpj) ok
creation_date ok
last_modification ok
is_active ok

# Pesquisar uma fazenda por:

nome do owner
document do owner
nome da fazenda
municipio
estado
id da fazenda

# Get Fazenda (retornar a fazenda):

Nome, id do proprietário, centro_id, área, município e estado

# Usar Swagger para fazer solicitações
