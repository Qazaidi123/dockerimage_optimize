pipeline {
  agent any

  
  environment {
    FRONT_IMAGE = "qazaidi123/myimage2"
    BACK_IMAGE = "qazaidi123/myimage"
    FRONT_CONTAINER = "optimize-front"
    BACK_CONTAINER = "optimize-back"
    IMAGE_TAG = "${BUILD_NUMBER}"
    DOCKER_CREDS = credentials('dockerhub-creds')
    
  }

  stages {

    stage("Code") {
      steps {
        git url: "https://github.com/Qazaidi123/dockerimagepush.git", branch: "main"
      }
    }

    stage("Build") {
      steps {
        sh '''
        docker build -t $FRONT_IMAGE:$IMAGE_TAG ./frontend
        docker build -t $BACK_IMAGE:$IMAGE_TAG ./backend
        '''
      }
    }

    

    stage("Image_Push") {
      steps {
        sh '''
        echo $DOCKER_CREDS_PSW | docker login -u $DOCKER_CREDS_USR --password-stdin
        docker push $FRONT_IMAGE:$IMAGE_TAG
        docker push $BACK_IMAGE:$IMAGE_TAG
        '''
      }
    }

    stage("Deploy") {
      steps {
        sh ''' 
        docker stop $FRONT_CONTAINER || true && docker rm $FRONT_CONTAINER || true
        docker stop $BACK_CONTAINER || true && docker rm $BACK_CONTAINER || true
        
        docker run -d --name $FRONT_CONTAINER -p 90:5000 $FRONT_IMAGE:$IMAGE_TAG
        docker run -d --name $BACK_CONTAINER -p 90:5000 $BACK_IMAGE:$IMAGE_TAG
      }
    }

    
  }
}

      
        
     
   

  

