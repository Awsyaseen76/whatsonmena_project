# build stage
FROM node:10.16.2-alpine as build-stage
WORKDIR /auth_service
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# production stage
FROM nginx:1.16.0-alpine as productions-stage
COPY --from=build-stage /auth_service/dist /usr/share/nginx/html
EXPOSE 80
CMD [ "nginx", "-g", "daemon off;" ]