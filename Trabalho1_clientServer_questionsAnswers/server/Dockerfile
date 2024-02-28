FROM mysql:5.7

# o scrip vai ser criado na hora da criação da imagem
COPY schema.sql /docker-entrypoint-initdb.d/

EXPOSE 3306

VOLUME ["/backup/"]