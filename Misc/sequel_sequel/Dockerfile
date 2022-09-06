FROM mysql:5.7.38-debian

RUN useradd -ms /bin/bash ethan
RUN echo "ethan:p4ssw0rd10" | chpasswd

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get -y update; apt-get -y install openssh-server

COPY sshd_config /etc/ssh/sshd_config
COPY mysqld.cnf /etc/mysql/mysql.conf.d/mysqld.cnf
COPY setup.sql /setup.sql

RUN mkdir /ftp
COPY sshd_config /ftp/sshd_config
COPY mysqld.cnf /ftp/mysqld.cnf
RUN sed 's/ictf{.*}/ictf{REDACTED}/g' /setup.sql > /ftp/setup.sql
RUN chmod -R 555 /ftp/

EXPOSE 22

CMD ["/bin/sh", "-c", "service mysql start && service ssh start && mysql -u root < /setup.sql && rm /setup.sql && bash"]
