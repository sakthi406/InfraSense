pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/sakthi406/InfraSense'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r app/requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t infrasense-app .'
            }
        }
    }
}