# Fast API exam

This module offers an API for querying a list of multiple-choice questions (MCQ). It is powered by FastAPI and runs under uvicorn.

## Module Organization

- Use of Pydantic to create data schemas.

- SQLite database to make easier data querying.

Below is the module's directory structure showing the important elements:

```
.
├── Dockerfile
├── README.md
├── __init__.py
├── app
│   ├── __init__.py
│   ├── databases.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── questions.py
│   │   ├── schemas.py
│   │   └── users.py
│   └── utils
│       ├── __init__.py
│       └── helpers.py
├── data
│   ├── qcm_database.db
│   └── questions.csv
|── example_requests.sh
├── ingest_data.py
├── main.py
├── requirements.txt
└── setup.sh
```

- `main.py`: This is the main script of the application. It serves as the entry point to launch the API.

- `ingest_data.py`: This is the script necessary for data ingestion. I use it here to load data from the CSV file into a SQLite database.

- `app`: This folder contains the source code of the application. It is divided into subfolders whose logic is to organize the application into databases, data models, and utilities.

- `databases.py`: Manages the connection to the database.

- `models`: This folder contains the definitions of models for users and questions.

- `Utils`: This folder contains auxiliary functions and improves the readability of the `main.py` program.

- `data`: This folder stores the data necessary for the application, including a SQLite database (`qcm_database.db`) with the original CSV file used for ingestion.

- `Dockerfile`: Dockerfile useful for containerizing the application.

- `requirements.txt`: This file lists the project's dependencies, making it easy to install them via pip.

- `setup.sh`: This shell script builds the Docker image and launches the container to facilitate the deployment of the application.

## Using the API

To use the API:

- Start by decompressing the archive.

```code
$ unzip examen_SOUILI.zip
```

- Then, grant execution permission to the `setup.sh` file.

```code
$ chmod +x ./setup.sh
```

- Next, run the `setup.sh` file and go to the address: `localhost:8000`

```code
$ ./setup.sh
```

> In the absence of an error message, the API is ready to be used.

You can test it using the examples available on the [openapi interface]() or consult this [file](example_requests.sh). Also, you need to grant the necessary permissions to this file `chmod +x ./example_requests.sh` before running it `example_requests.sh`.