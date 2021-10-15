pipeline {
   agent { label 'ubuntu-agent1' }

   environment {
     // You must set the following environment variables
     // ORGANIZATION_NAME
     // YOUR_DOCKERHUB_USERNAME (it doesn't matter if you don't have one)

     SERVICE_NAME = "stocks-app"
     REPOSITORY_TAG="${YOUR_DOCKERHUB_USERNAME}/${SERVICE_NAME}:${BUILD_ID}"
   }

   stages {
      stage('Preparation') {
         steps {
            cleanWs()
            git credentialsId: 'GitHub', url: "https://github.com/guysade/stocks.git"
         }
      }
      
      stage('Build and Push Image') {
         steps {
           sh 'docker image build --tag ${REPOSITORY_TAG} .'
         }
      }

      stage('Deploy to cluster using Helm'){
         steps {
           sh 'helm install stocks /stocksApp/stocksPackage/templates/deployment.yaml'
         }
      }
   }
}

