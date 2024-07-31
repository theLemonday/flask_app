pipeline {
    agent {
        docker {
            image: 'python:3.9-slim'
        }
    }

    stages {
        stage('build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('test') {
            steps {
                sh 'pytest /tests/tests_app.py'
            }
        }

    }
}
