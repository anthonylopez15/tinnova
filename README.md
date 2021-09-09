# Desafio Tinnova Software

- Foi criado um arquivo makefile para facilitar rodar os exercicios. Os exercicios de 1 a 4
se encontram na pasta /exercises.
  
# Importante
- É necessário ter uma maquina linux para poder rodar alguns comandos makefile , ter instalado 
o Docker e Docker Compose na sua maquina caso quera rodar localmente.
  
- Caso não tenha instalado o docker na sua maquina linux rode os seguintes comandos:

``` 
Instalação do Docker:

$ sudo su
$ curl https://releases.rancher.com/install-docker/19.03.sh | sh
$ usermod -aG docker ubuntu

Instalação do Docker Compose:

$ sudo su
$ apt-get install git -y
$ curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
$ chmod +x /usr/local/bin/docker-compose
$ ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```

### Rodar os exercicios 1 a 4

- Rode o seguinte comando: ``` make ex_1 ex_2 ex_3 ex_4 ```

## Testando a API
- Para esta ocasião foi disponiblizado um endereço ip onde o projeto encontra-se hospedado.

- SERVIDOR: http://35.198.47.55:3333/docs#/

- As endpoints podem ser testados com a ajuda do [Swagger](https://editor.swagger.io/).

- Em caso de rodar a aplicação localmente, será necessário o Docker estar instalado na máquina, 
e rodar os comandos:
  ``` 
  $ make build migrations start
  ```
- Ir até o endereço: http://localhost:3333/docs#/


 
