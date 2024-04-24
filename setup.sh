
# Création variable pour le nom et le tag de l'image
IMAGE_NAME=qcm_api
IMAGE_TAG=latest

# Vérifiez que l'image docker existe, sinon la construire. Lancer ensuite le container
if [ -z "$(docker images -q $IMAGE_NAME:$IMAGE_TAG)" ]; then
    echo "Docker image not found. Building the image..."
    
    docker image build . -t $IMAGE_NAME:$IMAGE_TAG -f Dockerfile
    
    if [ -z "$(docker images -q $IMAGE_NAME:$IMAGE_TAG)" ]; then
        echo "Failed to build the Docker image. Exiting."
        exit 1
    else
        echo "Docker image built successfully."
    fi
fi
# Lancer le container avec un fowarding de port sur 8000
docker run --rm --name $IMAGE_NAME -it -v $(pwd)/data:/api/data -p 8000:8000 $IMAGE_NAME:$IMAGE_TAG 
