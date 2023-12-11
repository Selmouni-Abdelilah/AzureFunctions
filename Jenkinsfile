pipeline {
    agent any
    tools {
        terraform "terraform"
    }
    environment {
        BLOB_TRIGGER = "blobtriggerfuncxxxx"
        RES_GROUP = "rg_abdel_proc" 
        BLOB_NAME = "blobnametrigger"
    }
    stages {
        stage('Checkout') {
            steps {
                script {
                    cleanWs()
                    checkout scmGit(branches: [[name: '*/BlobTrigger']], extensions: [], userRemoteConfigs: [[credentialsId: 'GitHubcredentials', url: 'https://github.com/Selmouni-Abdelilah/AzureFunctions']])
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
                            sh "terraform apply --auto-approve -var 'rg_name=${env.RES_GROUP}' -var 'function_name=${env.BLOB_TRIGGER}' -var 'blob_name=${env.BLOB_NAME}'"    

                    }
                }
            }
        }    
    
        stage('Deploy Blob trigger Function') {
            steps {
                script { 
                   dir('BlobTrigger') {
                        sh 'python3 -m pip install -r requirements.txt'
                        sh 'zip -r  blob.zip ./*'
                        sh "az functionapp deployment source config-zip -g ${env.RES_GROUP} -n ${env.BLOB_TRIGGER} --src blob.zip"                                   
                    }
                }
            }

        }

    }
}
