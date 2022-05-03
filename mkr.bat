docker-compose down
docker build -t  nya-archive-api ./nya-archive-api
docker build -t  nya-archive-web ./nya-archive-web
docker-compose up -d
