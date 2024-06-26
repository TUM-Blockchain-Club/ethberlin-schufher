# schuFHEr backend
The frontend is a flask powered project to define endpoints frontend call. For more infos see https://flask.palletsprojects.com/en/3.0.x/.


Backend is packaged inside a docker container based on a python:3.9-bullseye image and hosted with help of gunicorn (prod webserver for flask, see more: https://gunicorn.org/). For more details on configuration take a look at Dockerfile. Port mapping and establishing shared network with the frontend is done in the docker-compose.yml.

## Run dev
```bash
cd backend/src && flask run --debug
```
Make sure to install all dependencies prior. For this project, poetry  dependency management and packaging tool is used (https://python-poetry.org/).

## Notice on score api endpoint
We are using Zama library concrete-ml, which took us a long time to set up due to unstable compatibility with Apple Silicon and Docker. This is why we had to temporary use an Jupyter Notebook for that API. In the future, it will be completely integrated into Flask app.
