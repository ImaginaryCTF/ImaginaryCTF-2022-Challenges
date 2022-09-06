#!/bin/bash

docker build . -t sequel_sequel
docker run -tid -p 42022:22 -m 256m --restart=always sequel_sequel
