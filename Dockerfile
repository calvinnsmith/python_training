FROM python:alpine
COPY . /main
WORKDIR /main
CMD python python_data_structures.py
