This GitRepo reflects the Jenkinspipeline optimization by - (1) Alpine images (2) Parellel run of independent stages

# (1) By Alpine Images

# Frontend Dockerfile with alpine: FROM nginx:alpine (Image name: qazaidi123/myimage2:8) - frontend 
Total Image size: 24.87 MB , 

Image layer size : 3.69 MB  (First Layer: ADD alpine-minirootfs-3.23.4-x86_64.tar.gz / # buildkit) , 

Disk usage in EC2: 62.4 MB


# Backend Dockerfile with apine: FROM php-cli-alpine  (Image name: qazaidi123/myimage:2) - backend
Total Image size: 35.18 MB ,   

Image layer size : 3.69 MB  (First Layer: ADD alpine-minirootfs-3.23.4-x86_64.tar.gz / # buildkit) , 

Disk usage in EC2: 100 MB


# Frontend Dockerfile without alpine: FROM nginx:latest (Image name: qazaidi123/myimage2:9) - frontend
Total Image size: 60.18 MB , 

Image layer size : 28.4 MB  (First Layer: debian.sh --arch 'amd64' out/) , 

Disk usage in EC2: 161 MB

# Backend Dockerfile without apine: FROM php-cli-alpine  (Image name: qazaidi123/myimage:9) - backend
Total Image size: 171.35 MB ,     

Image layer size : 28.4 MB  (First Layer: debian.sh --arch 'amd64' out/) , 

Disk usage in EC2: 525 MB

# Jenkins pipeline stage time consumption
Image build stage from Dockerfile with alpine images:    1s , 

Image build stage from Dockerfile without alpine images: 19s , 

Container build (Deploy) stage from Dockerfile with alpine images: 836ms , 

Container build (Deploy) stage from Dockerfile with alpine images: 1s , 

Total Time consumption by pipeline with alpine image: 34s , 

Total Time consumption by pipeline with alpine image: 53s , 

Here the diffrence in time is not too much because the GitRepo, Dockerfiles and Jenkinsfile is kept simple
and is for learning purpose, but in real projects the alpine images may have big diffrence in time consumption of pipeline run.

# (2) By Parellalization (Very Effective):
Jenkins Pipeline optimization is also done by parellel run of independent stages. For e.g in Jenkinsfile Image build stage, frondend and backend image build is sequential i.e once the frontend image build is completed then only the backend build will start. Similary in Container run (Deploy), backend container run will start after the frontend container will be completed.
But in parellal run (jenkinsfile), frontend and backend image build will run parellal, similalry container run of both will also processed parellel. Therefore pipeline will take less time to complete.

Time taken by pipeline (Jenkinsfile) without parellel run:53s , 

Time taken by pipeline (jenkinsfile) with parellel run: 17s


# Screenshots: 
Alpine image optimization

# (1) Image Size

## Image size-DockerHUb
![DockerHub](screeshoot/Dockerhub_backendimage.jpg)

![DockerHub_Frontend](screeshoot/Dockerhub_frontendimage.jpg)

# (2) Diskspace by images on EC2
![Disk_space](screeshoot/images_diskspace.jpg)

# (3) Pipeline with and without Alpine images
![Pipeline_time](screeshoot/pipeline.jpg)

#  Parellalization Optimization
![Parellal_run](screeshoot/parellel_run.jpg)








