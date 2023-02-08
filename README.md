# Build docker image
docker build -t dockerapp .

# Run docker image with volume
docker run -v ${PWD}/data:/home/data dockerapp