

# Dockerfile with: FROM python 3.11-alpine   (Image name: qazaidi123/myimage:5 & 6)
Total Image size: 25.67 MB         
Image layer size : 3.69 MB  (First Layer: ADD alpine-minirootfs-3.23.4-x86_64.tar.gz / # buildkit)
Disk usage in EC2: 1.12 GB


# Dockerfile with: FROM python 3.11 (witout - alpine) (Image name: qazaidi123/myimage:3 & 4)
Total Image size: 396.2 MB
Image layer size : 47.03 MB  (First Layer: debian.sh --arch 'amd64' out/ 'trixie' '@1779062400')
Disk usage in EC2: 70.8 MB

