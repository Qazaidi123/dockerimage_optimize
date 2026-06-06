# "This repository demonstrates Jenkins pipeline optimization techniques using Alpine-based Docker images and parallel execution of independent stages.”

The goal is to reduce:
- Docker image size
  
- Pipeline execution time
  
- EC2 disk usage

  # Tech Stack
- Jenkins
- Docker
- DockerHub
- Nginx
- PHP
- AWS EC2
- GitHub

# (1) Optimization - Alpine Images

# Frontend Dockerfile with nginx:latest (Image name: qazaidi123/front_opt:2)
- Total Image size: 60.18 MB ,  
- Disk usage in EC2: 161 MB


# Backend Dockerfile with php:8.2 (Image name: qazaidi123/back_opt:2) 
- Total Image size: 171.35 MB ,   
- Disk usage in EC2: 525 MB


# Frontend Dockerfile nginx:alpine (Image name: qazaidi123/front_opt:3 )
- Total Image size: 24.83 MB, 
- Disk usage in EC2: 62.3 MB

# Backend Dockerfile php:8.2-cli-alpine  (Image name: qazaidi123/back_opt:3) 
- Total Image size: 35.18 MB ,     
- Disk usage in EC2: 100 MB

# Pipeline run-time comparison
- Image build stage from Dockerfile with alpine images: 10 sec    , 
- Image build stage from Dockerfile without alpine images: 18 sec , 
 

Note:

Since the application is intentionally lightweight for learning purposes, the runtime difference in image build is moderate. In large-scale production projects, Alpine images can significantly reduce pipeline execution time and storage usage.

# (2) By Parellalization i.e Parellal jenkins stages (Very Effective):
Jenkins Pipeline optimization is also done by parellel run of independent stages. 
- Sequential run (Jenkinsfile): Frontend and Backend images build runs one after the another i.e once the frontend image build is completed then only the backend build will start. Similary in Container run (Deploy), backend container run will start after the frontend container will be completed.
- Parellal run (jenkinsfile): Frontend and backend image build will run simultaneously using parallel stages. Similalry container run of both images will also processed simultanously. Therefore pipeline will take less time to complete.

## Parelllalization results:

- Sequential mode :57s , 

- Parellel run: 28s

# Jenkins Pipeline Features
- GitHub integration
- Automated Docker image build
- Parallel frontend/backend image builds
- DockerHub image push
- Automated container deployment
- CI/CD runtime optimization

# Key Learnings
- Alpine images reduce Docker image size and Disk Usage (storage).
- Smaller images improve pipeline efficiency as Image build take less time.
- Parallel Jenkins stages significantly reduce pipeline runtime.
- CI/CD optimization improves scalability and deployment efficiency.




# Screenshots: 

DockerHub-Backend

![DockerHub_frontend](screenshots/DockerHubBack.png)

DockerHub-Frontend

![DockerHub_backend](screenshots/DockerHubFront.png)

Diskspace usage by Images- Alpine vs normal Images

![Disk_space](screenshots/EC2images.png)

 Pipeline time consumptiom with and without Alpine images
 
![Pipeline_time](screenshots/pipelineImageOpt.png)

Parallelization Pipeline time

![Parellal_run](screenshots/parallel.png)








