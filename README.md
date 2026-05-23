This GitRepo reflects the Jenkinspipeline optimization by - (1) Alpine images (2) Parellel run of independent stages

# Frontend Dockerfile with alpine: FROM nginx:alpine (Image name: qazaidi123/myimage2:8) - frontend 
Total Image size: 24.87 MB         
Image layer size : 3.69 MB  (First Layer: ADD alpine-minirootfs-3.23.4-x86_64.tar.gz / # buildkit)
Disk usage in EC2: 62.4 MB


# Backend Dockerfile with apine: FROM php-cli-alpine  (Image name: qazaidi123/myimage:2) - backend
Total Image size: 35.18 MB         
Image layer size : 3.69 MB  (First Layer: ADD alpine-minirootfs-3.23.4-x86_64.tar.gz / # buildkit)
Disk usage in EC2: 100 MB


# Frontend Dockerfile without alpine: FROM nginx:latest (Image name: qazaidi123/myimage2:9) - frontend
Total Image size: 60.18 MB
Image layer size : 28.4 MB  (First Layer: debian.sh --arch 'amd64' out/)
Disk usage in EC2: 161 MB

# Backend Dockerfile without apine: FROM php-cli-alpine  (Image name: qazaidi123/myimage:9) - backend
Total Image size: 171.35 MB         
Image layer size : 28.4 MB  (First Layer: debian.sh --arch 'amd64' out/)
Disk usage in EC2: 525 MB

# Jenkins pipeline stage time consumption
Image build stage from Dockerfile with alpine images:    1s
Image build stage from Dockerfile without alpine images: 19s

Container build (Deploy) stage from Dockerfile with alpine images: 836ms
Container build (Deploy) stage from Dockerfile with alpine images: 1s

Here the diffrence is looking to be not too much because the GitRepo, Dockerfiles and Jenkinsfile is kept simmple
and is for learning purpose, but in real projects the alpine images may have big diffrence in time consumption of pipeline run.

