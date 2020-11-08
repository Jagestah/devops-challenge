FROM python:3.7.9-slim
ADD ./requirements.txt .
COPY . .
RUN pip3 install -r requirements.txt    
CMD python integration.py