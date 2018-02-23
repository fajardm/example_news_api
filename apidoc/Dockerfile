#Uncomment this for develop
#FROM nginx:alpine

#Uncomment this for heroku
FROM nginx:stable

COPY default.conf.template /etc/nginx/conf.d/default.conf.template

COPY . /usr/share/nginx/html

#Uncomment this for heroku
CMD /bin/bash -c "envsubst \\\$PORT < /etc/nginx/conf.d/default.conf.template > /etc/nginx/conf.d/default.conf && nginx -g 'daemon off;'"