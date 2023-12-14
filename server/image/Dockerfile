FROM ubuntu:22.04
RUN apt-get update; apt-get install -y wget curl openjdk-8-jdk python3-pip net-tools lsof nano
RUN pip3 install jupyterlab==3.4.5 MarkupSafe==2.0.1 cassandra-driver pyspark==3.2.2 flask openai python-dotenv

# SPARK
RUN wget https://archive.apache.org/dist/spark/spark-3.2.2/spark-3.2.2-bin-hadoop3.2.tgz; tar -xf spark-3.2.2-bin-hadoop3.2.tgz; rm spark-3.2.2-bin-hadoop3.2.tgz

# CASSANDRA
RUN wget https://archive.apache.org/dist/cassandra/4.0.7/apache-cassandra-4.0.7-bin.tar.gz; tar -xf apache-cassandra-4.0.7-bin.tar.gz; rm apache-cassandra-4.0.7-bin.tar.gz

ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
ENV PATH="${PATH}:/apache-cassandra-4.0.7/bin:/spark-3.2.2-bin-hadoop3.2/bin"
#ENV PATH="${PATH}:/apache-cassandra-4.0.7/bin"
CMD ["sh", "/start.sh"]