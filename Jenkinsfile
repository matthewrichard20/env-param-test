pipeline{
    agent any
    parameters {
        string(name: 'dbName', defaultValue: 'devops-rds-staging2', description: '')
        password(name: 'snapRole')
        password(name: 'exportRole')
        password(name: 'kms')
    }
    stage('Build Env'){
    sh label: '', script: '''
    echo ASSUME_ROLE=${snapRole} >> .env
    echo EXPORT_ROLE=${exportRole} >> .env
    echo KMS_KEY=${kms} >> .env
    dan seterusnya
    '''
    }
    stage('test Py'){
      sh "/Users/RichardMatthew/miniconda3/bin/python3 env-test.py"
    }

    stage('clean up'){
      sh "rm .env"
    }
}