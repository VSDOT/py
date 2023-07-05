FROM maven as mv

WORKDIR /usr/src/mymaven

COPY . .  

RUN mvn clean package 

#RUN .mvn\wrapper\maven-wrapper.jar"

###################################################

FROM openjdk:21-ea-8-jdk-slim-buster

WORKDIR /webapps

COPY --from=mv /usr/src/mymaven/target/*.jar .

RUN mv /webapps/*.jar /webapps/app.jar

VOLUME mybridge

EXPOSE 8080/tcp

CMD ["java", "-jar",  "/webapps/app.jar"]
#####################
###############
##########
#####
#


