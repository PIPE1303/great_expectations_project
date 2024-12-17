pipeline {
    agent {
        docker {
            image 'python:3.9' // Imagen con Python preinstalado
        }
    }
    stages {
        stage('Setup Environment') {
            steps {
                sh 'python -m venv venv'
            }
        }
        stage('Validate File') {
            steps {
                sh './venv/bin/python validate_file.py'
            }
        }
    }
}