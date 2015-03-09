FROM centos:6

RUN rpm -Uvh http://ftp.linux.ncsu.edu/pub/epel/6/i386/epel-release-6-8.noarch.rpm
RUN yum -y install http://yum.basho.com/gpg/basho-release-6-1.noarch.rpm

RUN yum -y update
RUN yum -y install riak
RUN yum -y install sudo
RUN sed '/requiretty/d' /etc/sudoers
ADD . /etc/riak
EXPOSE 8087
EXPOSE 8098
