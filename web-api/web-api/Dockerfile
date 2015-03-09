FROM centos:6

RUN rpm -Uvh http://ftp.linux.ncsu.edu/pub/epel/6/i386/epel-release-6-8.noarch.rpm

RUN yum -y update
RUN yum -y install python-pip
RUN yum -y groupinstall "Development Tools"
RUN yum -y install python-devel
RUN yum -y install libffi-devel
RUN yum -y install openssl-devel

RUN mkdir -p /var/www/src
ADD src/ /var/www/src
WORKDIR /var/www/src
RUN pip install -r requirements.txt
