

# Dockerfile with: FROM nginx:alpine (Image name: qazaidi123/myimage2:8) - frontend 
Total Image size: 24.87 MB         
Image layer size : 3.69 MB  (First Layer: ADD alpine-minirootfs-3.23.4-x86_64.tar.gz / # buildkit)
Disk usage in EC2: 62.4 MB


# Dockerfile with: FROM php-cli-alpine  (Image name: qazaidi123/myimage:2)
Total Image size: 35.18 MB         
Image layer size : 3.69 MB  (First Layer: ADD alpine-minirootfs-3.23.4-x86_64.tar.gz / # buildkit)
Disk usage in EC2: 100 MB


# Dockerfile with: FROM python 3.11 (witout - alpine) (Image name: qazaidi123/myimage:3 & 4)
Total Image size: 396.2 MB
Image layer size : 47.03 MB  (First Layer: debian.sh --arch 'amd64' out/ 'trixie' '@1779062400')
Disk usage in EC2: 70.8 MB

