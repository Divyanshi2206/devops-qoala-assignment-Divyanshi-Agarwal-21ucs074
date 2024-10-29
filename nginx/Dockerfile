# FROM nginx:latests
# COPY nginix.conf /etc/nginx/nginx.conf
# COPY ./html /usr/share/nginx/htmll
# EXPOSE "eighty"
# CMD ["nginx", "-g", "daemon of;"]

FROM nginx:latest
COPY nginx.conf /etc/nginx/nginx.conf
COPY ./html /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

