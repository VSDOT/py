FROM nginx
 
WORKDIR /tmp

COPY . .

RUN rm /usr/share/nginx/html/index.html \
    && cp -r /tmp/* /usr/share/nginx/html
    

EXPOSE 80/tcp
