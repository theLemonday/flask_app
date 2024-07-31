pipeline {
    agent {
        dockerfile true
    }

    stages {
        stage('test') {
            steps {
                sh 'pytest tests/tests_app.py'
            }
        }

    }
}
