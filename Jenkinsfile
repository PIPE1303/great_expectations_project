pipeline {
    agent any
    stages {
        stage('Setup Environment') {
            steps {
                sh 'python3 -m venv venv'
            }
        }
        stage('Validate File') {
            steps {
                sh './venv/bin/python scripts/validate_file.py'
            }
        }
    }
}