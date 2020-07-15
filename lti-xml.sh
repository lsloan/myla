#!/usr/bin/env bash

if [ $# -ne 2 ]; then
  echo $0 LAUNCH_HOSTNAME APP_NAME > /dev/tty
  exit 1
fi

export LAUNCH_HOSTNAME=$1
export APP_NAME=$2
envsubst \$LAUNCH_HOSTNAME,\$APP_NAME < lti_template.xml
