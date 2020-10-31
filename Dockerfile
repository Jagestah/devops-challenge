FROM python:3.7.9-slim
ADD ./requirements.txt .
COPY . .
RUN pip3 install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD ["integration.py"]