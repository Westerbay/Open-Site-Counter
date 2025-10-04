# Open Site Counter

Open Site Counter is a FastAPI-based API that allows:
- registering website visits (`/register`),
- retrieving statistics and a connection graph (`/get`).

## Features
- SQLite storage with SQLAlchemy
- Hashing for efficient lookups
- `/register` endpoint to log visits
- `/get` endpoint to return stats and connection graphs
- `frontend` folder, showcasing an example of how to use the application

## Requirements
- Python 3.10+ or Docker

## Installation (without Docker)
```bash
chmod +x run.sh
./run.sh
```

The API will be available at [http://127.0.0.1:5001](http://127.0.0.1:5001).

## Usage with Docker

1. Build the Docker image:
```bash
docker build -t open-site-counter .
```

2. Run the container exposing port 5001:
```bash
docker run -d -p 5001:5001 open-site-counter
```

You can also pull and use the prebuilt Docker image from the GitHub page.
