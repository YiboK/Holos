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
Build Docker image:
```
docker build -t holos-image ./image
```

Start docker containers:
```
docker compose up -d
```

List the container mapping localhost:5000->localhost:5000
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
Now the backend should be on localhost:5000

To insert data into database, send POST request to /insert
To get top N subjects in database, send GET request to /topn
To get top N topics by subject, send GET request to /topnsubject