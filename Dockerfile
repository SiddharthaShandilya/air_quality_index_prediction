FROM python:latest
RUN apt-get update
RUN python -m pip install --upgrade pip
COPY . /aqt
EXPOSE 5000
WORKDIR /aqt
RUN pip install -r requirements.txt

RUN dvc dag | cat > dvc_dag_image.txt
#RUN echo " dvc repro" > air_quality_index_prediction/dvc.sh
RUN cat dvc_dag_image.txt
RUN dvc repro dvc.yaml