FROM tensorflow/tensorflow:latest
MAINTAINER siddharthashandilya104@gmail.com
RUN apt-get update
RUN apt-get install -y git

RUN /usr/bin/python3 -m pip install --upgrade pip
RUN git clone https://github.com/SiddharthaShandilya/air_quality_index_prediction.git
#RUN echo
RUN cd air_quality_index_prediction
RUN pip install -r air_quality_index_prediction/requirements.txt


