FROM node:16-alpine3.11

RUN npm install -g http-server

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

RUN npm run build

