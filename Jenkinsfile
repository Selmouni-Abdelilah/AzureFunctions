pipeline {
    agent any
    tools {
        terraform "terraform"
    }
    environment {
        HTTP_TRIGGER = "httptriggerfuncxxxx"  
        RES_GROUP = "rg_abdel_proc" 
        BLOB_NAME = "blobnametrigger"
        QUEUE_NAME = "queuenametrigger"
    }
    stages {
        stage('Checkout') {
            steps {
                script {
                    cleanWs()
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'GitHubcredentials', url: 'https://github.com/Selmouni-Abdelilah/AzureFunctions']])
                }
            }
        }
        stage('Azure login'){
            steps{
                withCredentials([azureServicePrincipal('Azure_credentials')]) {
                    sh 'az login --service-principal -u $AZURE_CLIENT_ID -p $AZURE_CLIENT_SECRET -t $AZURE_TENANT_ID'
                }
            }
        }
        stage('Terraform ') {
            steps {
                script {
                    dir('Terraform') {
                            sh 'terraform init -upgrade'
                            sh "terraform apply --auto-approve -var 'rg_name=${env.RES_GROUP}' -var 'function_name=${env.HTTP_TRIGGER}' -var 'blob_name=${env.BLOB_NAME}' -var 'myqueue_name=${env.QUEUE_NAME}'"
                    }
            }
            }
        }    
    
        stage('Deploy Function') {
            steps {
                script { 
                   dir('httpTrigger') {
                        sh 'python -m pip install -r requirements.txt'
                        sh 'zip -r  http.zip ./*'
                        sh "az functionapp deployment source config-zip -g ${env.RES_GROUP} -n ${env.HTTP_TRIGGER} --src http.zip"    
                    
                                   
                    }
                }
            }

        }

    }
}