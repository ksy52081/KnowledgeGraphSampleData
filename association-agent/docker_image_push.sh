REGISTRY="balab.harbor.com"
IMAGE_NAME="datafabric/agent:v1.0"
IMAGE_FULL_NAME="$REGISTRY/$IMAGE_NAME"

docker build -t "$IMAGE_FULL_NAME" .
docker push "$IMAGE_FULL_NAME"