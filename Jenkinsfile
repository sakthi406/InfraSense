pipeline {
    agent {
        docker {
            image 'python:3.10'
        }
    }

    stages {

        stage('Install Dependencies') {
            steps {
                sh 'pip install --user -r app/requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                export PATH=$HOME/.local/bin:$PATH
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