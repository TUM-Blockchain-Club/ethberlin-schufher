# SCHUFHER
SCHUFA, but keep your data to yourself

## Setup

`docker compose up --build`.

(if poetry complains, run `poetry lock` in the backend folder)

The frontend and bank data API are started this way, the ML model is run in a separate jupyter notebook since it would not run directly on Apple Silicon.

The frontent can be accessed at `localhost:8888`.
