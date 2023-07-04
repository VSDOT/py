FROM node:12.7-alpine AS build

WORKDIR /usr/src/app

COPY package.json package-lock.json ./

RUN npm install

COPY . .

RUN npm run build

EXPOSE 4200

VOLUME New_volume

### STAGE 2: Run ###
FROM nginx:1.17.1-alpine

WORKDIR /app

COPY nginx.conf /etc/nginx/nginx.conf

COPY --from=build /usr/src/app/dist/aston-villa-app /usr/share/nginx/html

CMD ["npm", "start"]
