#! /bin/bash
# Tag, Push and Deploy only if it's not a pull request
if [ "$TRAVIS_BRANCH" == "master" ]; then
    docker login --username "$DOCKER_USERNAME" --password "$DOCKER_PASSWORD"
    docker push pdxdiver/django-web:latest
    ecs-cli compose --project-name ecs-hacko --file ecs-deploy.yml service up;
fi
