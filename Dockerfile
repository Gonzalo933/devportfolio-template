FROM node:slim
WORKDIR /opt
VOLUME /opt/dist

#COPY libs libs/
COPY scss/ scss/
COPY js/ js/
COPY package.json gulpfile.js ./
# Separate layer for index as it is modified often
RUN npm install
ENTRYPOINT ["npm", "run", "build"]