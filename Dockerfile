FROM python:3.12.9-alpine
WORKDIR /src
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python3", "server.py"]
