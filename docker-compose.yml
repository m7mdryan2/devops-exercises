version: '3'
services:
  mongo:
    image: mongo:latest
    ports:
      - "27017:27017"
  flask:
    build: .
    ports:
      - "5000:5000"
    depends_on:
      - mongo
    environment:
      MONGO_HOST: mongo
      MONGO_PORT: 27017
      MONGO_DB: mydatabase
      MONGO_COLLECTION: mycollection
