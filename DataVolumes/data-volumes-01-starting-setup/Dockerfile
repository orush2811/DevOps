FROM node:14

ARG DEFAULT_PORT=80

WORKDIR /HTMLPage

COPY package.json /HTMLPage/

RUN npm install

COPY . .

ENV PORT $DEFAULT_PORT

EXPOSE $PORT 80


CMD ["npm","start"]