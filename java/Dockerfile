FROM maven:3.5.2-jdk-8-alpine

COPY . /usr/src/home
 
WORKDIR /usr/src/home

RUN mvn package

FROM maven:3.5.2-jdk-8-alpine

WORKDIR /root/

COPY . /usr/src/home/taeget/app.war 

EXPOSE 8080

VOLUME /var/log/app

ENTRYPOINT ["java',"war","./app.war"]
