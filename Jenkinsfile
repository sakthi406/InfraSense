pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                sh '''
                apt update
                apt install -y python3 python3-pip
                pip3 install -r app/requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                export PYTHONPATH=.
                pytest
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t infrasense-app .'
            }
        }
    }
}