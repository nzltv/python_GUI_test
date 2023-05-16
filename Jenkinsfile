pipeline {
    agent {
        label 'python'
    }
    stages {
        stage('Run Python Script') {
            steps {
                sh 'python3 test_pywin.py'
            }
        }
    }
}