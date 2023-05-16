pipeline {
    agent {
        label 'test-machine'
    }
    stages {
        stage('Run Python Script') {
            steps {
                bat 'python3 test_pywin.py'
            }
        }
    }
}
