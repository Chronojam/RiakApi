FROM centos:6

RUN rpm -Uvh http://ftp.linux.ncsu.edu/pub/epel/6/i386/epel-release-6-8.noarch.rpm

RUN yum -y update
RUN yum -y install nginx

RUN service nginx stop

ADD nginx.conf /etc/nginx/nginx.conf
