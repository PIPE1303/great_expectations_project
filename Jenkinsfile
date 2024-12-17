pipeline {
    agent any
    stages {
        stage('Setup Environment') {
            steps {
                sh 'python -m venv venv'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }
        stage('Validate File') {
            steps {
                sh './venv/bin/python scripts/validate_file.py'
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'data/raw/*.csv', onlyIfSuccessful: true
        }
        failure {
            echo 'Validation failed. Check logs for details.'
        }
    }
}