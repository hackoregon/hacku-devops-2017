#!/bin/bash
# Download, Install and Configure ecs-cli
sudo curl -o /usr/local/bin/ecs-cli https://s3.amazonaws.com/amazon-ecs-cli/ecs-cli-linux-amd64-latest
sudo chmod +x /usr/local/bin/ecs-cli

ecs-cli configure \
  --region us-west-2 \
  --access-key $AWS_ACCESS_KEY \
  --secret-key $AWS_SECRET_KEY  \
  --cluster ecs-hacko \
  --compose-project-name-prefix " " \
  --compose-service-name-prefix " " \
  --cfn-stack-name-prefix " "
