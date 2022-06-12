FROM node:14-alpine3.16
COPY ./ /app
WORKDIR /app
RUN npm install && npm run build

FROM nginx:1.22.0-alpine
RUN mkdir /app
COPY --from=0 /app/dist /app
COPY nginx.conf /etc/nginx/nginx.conf
