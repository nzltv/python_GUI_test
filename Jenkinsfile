pipeline {
    agent {
        label 'test-machine'
    }
    stages {
        stage('Run Python Script') {
            steps {
                sh (
                    script: 'python test_pywin.py',
                    returnStatus: true
                )
            }
        }
    }
}
