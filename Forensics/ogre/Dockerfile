FROM node:18-alpine

WORKDIR /app
RUN mkdir ogre
WORKDIR /app/ogre

RUN npm init -y
RUN echo aWN0ZntvbmlvbnNfaGF2ZV9sYXllcnNfaW1hZ2VzX2hhdmVfbGF5ZXJzfQo= > /tmp/secret
RUN npm install express
RUN rm /tmp/secret
RUN npm install ejs

COPY server.js server.js
COPY views views
COPY public public
COPY quotes.json quotes.json

EXPOSE 8080
CMD [ "node", "server.js" ]