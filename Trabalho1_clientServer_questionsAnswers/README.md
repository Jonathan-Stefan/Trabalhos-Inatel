### Subindo o container
* Build
```
docker build -t flask-client .
```
```
docker build -t mysql-serve .
```

* Criando o network (comunicação entre containers)
```
docker network create flasknetwork
```

* Subindo a imagem
```
docker run -d -p 5000:5000 --name flask-container --network flasknetwork flask-client
```
```
docker run -d -p 3307:3306 --name mysql-container --network flasknetwork -e MYSQL_ALLOW_EMPTY_PASSWORD=True mysql-serve
```