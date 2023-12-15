# Holos

## Website
Make sure installed node.js and react

Build project:
```
npm install
```

Run on localhost:
```
npm run dev
```

## Backend
Build docker image:
```
docker build -t holos-image ./image
```

Start docker containers:
```
docker compose up -d
```

List all contaienrs and find container mapping localhost:5000->localhost:5000
```
docker compose ps -a
```

Switch to that container's shell
```
docker exec -it <CONTAINER NAME> bash
```

Go to the notebooks folder:
```
cd notebooks
```

Run backend:
```
python3 server.py
```
Now the backend should be on 0.0.0.0:5000

To insert data into database, send POST request to /insert and request body should be like {'subject': "", 'topic': "", 'id': "",'duration':""}
To get top N subjects in database, send GET request to /topn?n=(?)
To get top N topics by subject, send GET request to /topntopics?n=(?)subject=(?)