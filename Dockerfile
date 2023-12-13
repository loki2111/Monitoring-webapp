FROM python:3.8-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
ENV FLAST_RUN_HOST=0.0.0.0
EXPOSE 5000
CMD ["flask", "run"]
