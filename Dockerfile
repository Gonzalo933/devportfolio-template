FROM node:slim
WORKDIR /opt
VOLUME /opt/dist

COPY scss/ scss/
COPY js/ js/
COPY package.json gulpfile.js ./
RUN npm install
ENTRYPOINT ["npm", "run", "build"]