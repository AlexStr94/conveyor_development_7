FROM python:3.12-slim
WORKDIR /app
COPY auth/ auth/
COPY auth_server.py auth_server.py 
COPY requirements.txt requirements.txt
COPY constants.py constants.py
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "auth_server.py" ]