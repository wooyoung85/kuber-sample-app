FROM openjdk:8-jdk-alpine

# Django Application url 환경변수로 정의
# local pc ip 는 ifconfig를 통해 확인
#ENV DJANGO_APP_URL http://<local pc ip>:8000
ADD target/sentiment-analysis-0.0.1-SNAPSHOT.jar /
EXPOSE 8080
CMD ["java", "-jar", "sentiment-analysis-0.0.1-SNAPSHOT.jar", "--django_app.url=${DJANGO_APP_URL}"]