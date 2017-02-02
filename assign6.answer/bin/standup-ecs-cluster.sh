#!/bin/bash
ecs-cli up \
  --keypair dan-ecs-west \
  --capability-iam \
  --size 1 \
  --instance-type t2.large  \
  --port 8000 \
