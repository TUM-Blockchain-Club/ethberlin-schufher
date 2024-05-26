# schuFHEr frontend
The frontend is a vite powered project that was done set up with help of create-vue tool. For more infos see https://github.com/vuejs/create-vue.

The pages are located in the src/views folder and are routed in src/router/index.js.

Frontend is packaged inside a docker container based on a node:lts-alpine image and hosted with help of nginx. For more details on configuration take a look at Dockerfile and nginx.conf accordingly. Port mapping and establishing shared network with the backend is done in the docker-compose.yml.

## Run dev
```bash
cd vue && npm run dev 
```
