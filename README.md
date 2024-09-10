# fishregression
- from sklearn.linear_model import LinearRegression
- FastApi

### run - dev
```bash
$ uvicorn src.fr.main:app --reload
```

### git add,push tag
```bash
$ git tag 0.2.0
$ git push origin 0.2.0
```

### docker
```bash
$ sudo docker build -t fishregression:0.2.0 .
$ sudo docker run -d --name fr020 -p 8020:8080 fishregression:0.2.0
```

### api endpoint
```bash
$ curl -X 'GET' \
  'http://localhost:8020/fish?length=30.333' \
  -H 'accept: application/json'


```
