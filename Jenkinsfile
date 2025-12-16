pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            steps {
                sh 'python -m py_compile source/jar.py'
                stash(name: 'compiled', includes: 'source/*.py*')
            }
        }
        stage('Test') {
            steps {
                sh 'py.test --junit-xml test/reports/results.xml test/test_jar.py'
            }
            post {
                always {
                    junit 'test/reports/results.xml'
                }
            }
        }
        stage('Deliver') {
            steps {
                sh "pyinstaller --onefile source/jar.py"
            }
            post {
                success {
                    archiveArtifacts 'ship/jar_exec'
                }
            }
        }
    }
}