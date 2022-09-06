# syntax=docker/dockerfile:1

FROM node:18-alpine
ENV NODE_ENV=production
WORKDIR /app
COPY ["package.json", "package-lock.json*", "./"]
RUN npm install --production

COPY index.js index.js
COPY Dockerfile.release Dockerfile
COPY public public
COPY flag.txt FL46_7BVY31.7X7

EXPOSE 3000
CMD ["node", "index.js", "server"]
