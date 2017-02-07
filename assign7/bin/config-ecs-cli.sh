#!/usr/bin/env bash
# Download, Install and Configure ecs-cli

if [ "$(uname)" == "Darwin" ]; then
  # Get the Mac binaries
  sudo curl -o /usr/local/bin/ecs-cli https://s3.amazonaws.com/amazon-ecs-cli/ecs-cli-darwin-amd64-latest
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
  #Get the L binaries
  sudo curl -o /usr/local/bin/ecs-cli https://s3.amazonaws.com/amazon-ecs-cli/ecs-cli-linux-amd64-latest
fi
sudo chmod +x /usr/local/bin/ecs-cli


ecs-cli configure \
  --region us-west-2 \
  --access-key $AWS_ACCESS_KEY \
  --secret-key $AWS_SECRET_KEY  \
  --cluster assign7-hacko \
  --compose-project-name-prefix " " \
  --compose-service-name-prefix " " \
  --cfn-stack-name-prefix " "
