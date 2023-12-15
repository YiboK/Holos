# Holos

## Set up Website
Make sure installed node.js and react

Build project:
```
npm install
```

Run on localhost:
```
npm run dev
```

## Set up Backend
### This backend contain a python server and Cassandra database. This backend collect user data and allow front-end to display most popular data in the database

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


## Frontend
This project enables the user to move around, interact, and communicate with the AI by voice in the VR world, and enables the user to conveniently generate a learning plan by answering questions posed by the AI.
In addition, this project presets five subject models. Users can click on the models to get the hot topics of the corresponding subjects. They can explore the direction of learning through this recommendation system.

In the future, we may further improve AI to make it more innovative and easier to use. Also, make it provide learning materials rather than just learning schema without violating copyright.

Download Unity Project from google drive:
```
https://drive.google.com/file/d/17HDTqG4wMeF8b54MH7DXGJmRQplgNSDT/view?usp=drive_link
```

Open Unity and add project from local disk.

Connect Meta Quest 3 Headset to PC through cable.

Launch the Oculus Quest Link.

Run the Unity Project.
