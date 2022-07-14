from ubuntu
RUN apt-get update && apt-get install --no-install-recommends --no-install-suggests -y curl ca-certificates
WORKDIR /app/data
COPY script.sh /app/data/script.sh
RUN chmod +x script.sh


