# Holos

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

### Whisper GPT
The program is avaible individually [here](https://github.com/YiboK/whisperGPT).

Since the OpenAI is constantly updating their API, I changed something in packages for multiple times (The lastest update: 12/15/2023).

#### Setting Up Your OpenAI Account
To use the OpenAI API, you need to have an OpenAI account. Follow these steps to create an account and generate an API key:

- Go to https://openai.com/api and sign up for an account
- Once you have created an account, go to https://beta.openai.com/account/api-keys
- Create a new secret key and save it

#### Saving Your Credentials
To make requests to the OpenAI API, you need to use your API key and organization name (if applicable). To avoid exposing your API key in your Unity project, you can save it in your device's local storage.

To do this, follow these steps:

- Create a folder called .openai in your home directory (e.g. `C:User\UserName\` for Windows or `~\` for Linux or Mac)
- Create a file called `auth.json` in the `.openai` folder
- Add an api_key field to the auth.json file and save it
- Here is an example of what your auth.json file should look like:

```json
{
    "api_key": "sk-...W6yi"
}
```

**IMPORTANT:** Your API key is a secret. 
Do not share it with others or expose it in any client-side code (e.g. browsers, apps). 
If you are using OpenAI for production, make sure to run it on the server side, where your API key can be securely loaded from an environment variable or key management service.

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

