pipeline{
    agent any
    parameters {
        string(name: 'dbName', defaultValue: 'devops-rds-staging2', description: '')
        password(name: 'snapRole')
        password(name: 'exportRole')
        password(name: 'kms')
    }
    stages {
        stage('Build Env'){
            steps{
                sh label: '', script: '''
                echo ASSUME_ROLE=${snapRole} >> .env
                echo EXPORT_ROLE=${exportRole} >> .env
                echo KMS_KEY=${kms} >> .env
                '''
            }
        
        }
        stage('test Py'){
            steps {
                sh "/Users/RichardMatthew/miniconda3/bin/python3 env-test.py"
            }
        
        }

        stage('clean up'){
            steps {
                sh "rm .env"
            }
        
        }

    }
    
}