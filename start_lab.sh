#!/usr/bin/bash

docker run \
  --volume=/var/lib/drone:/data \
  --env=DRONE_GITHUB_CLIENT_ID=1fd79abceaadb2b3cd6d \
  --env=DRONE_GITHUB_CLIENT_SECRET=c8aa7b02b6df54c8b4a3181bed3f563349ba776d \
  --env=DRONE_RPC_SECRET=6019a80e21066d906446b45a6eac1c2c \
  --env=DRONE_SERVER_HOST="$1" \
  --env=DRONE_SERVER_PROTO=https \
  --publish=80:80 \
  --publish=443:443 \
  --restart=always \
  --detach=true \
  --name=drone \
  drone/drone:2

docker run --detach \
  --volume=/var/run/docker.sock:/var/run/docker.sock \
  --env=DRONE_RPC_PROTO=https \
  --env=DRONE_RPC_HOST="$1" \
  --env=DRONE_RPC_SECRET=6019a80e21066d906446b45a6eac1c2c \
  --env=DRONE_RUNNER_CAPACITY=2 \
  --env=DRONE_RUNNER_NAME=my-first-runner \
  --publish=3000:3000 \
  --restart=always \
  --name=runner \
  drone/drone-runner-docker:1
