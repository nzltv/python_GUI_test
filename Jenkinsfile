pipeline {
    agent {
        label 'test-machine'
    }
    stages {
        stage('Run Python Script') {
            steps {
                bat 'python test_pywin.py'
            }
        }
    }
}
