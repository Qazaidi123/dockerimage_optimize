pipeline {
  agent any

  
  environment {
    FRONT_IMAGE = "qazaidi123/frontimage"
    BACK_IMAGE = "qazaidi123/backimage"
    FRONT_CONTAINER = "frontcon"
    BACK_CONTAINER = "backcon"
    IMAGE_TAG = "${BUILD_NUMBER}"
    DOCKER_CREDS = credentials('dockerhub-creds')
    
  }

  stages {

    stage("Gitrepo clone") {
      steps {
        git url: "https://github.com/Qazaidi123/dockerimage_optimize.git", branch: "main"
      }
    }

    stage("Build") {
      steps {
        sh '''
        docker build -t $FRONT_IMAGE:$IMAGE_TAG ./fontend
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
        docker run -d --name $BACK_CONTAINER -p 91:5000 $BACK_IMAGE:$IMAGE_TAG
        '''
      }
    }

    
  }
}

      
        
     
   

  

