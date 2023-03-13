FROM python:3.11.1
EXPOSE 5000
WORKDIR /app
RUN pip install pygeoif==0.7 flask satellite-czml python-dateutil
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]
