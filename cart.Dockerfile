FROM python:3.12-slim
WORKDIR /app
COPY cart/ cart/
COPY auth/ auth/
COPY cart_server.py cart_server.py 
COPY requirements.txt requirements.txt
COPY constants.py constants.py
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "cart_server.py" ]