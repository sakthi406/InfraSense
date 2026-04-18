pipeline {
    agent none 

    stages {

        stage('Test') {
            agent {
                docker {
                    image 'python:3.10'
                }
            }
            steps {
                sh '''
                export HOME=/tmp
                pip install --user -r app/requirements.txt
                export PATH=$HOME/.local/bin:$PATH
                export PYTHONPATH=.
                pytest
                '''
            }
        }

        stage('Build Docker Image') {
            agent any   
            steps {
                sh 'docker build -t infrasense-app .'
            }
        }
    }
}