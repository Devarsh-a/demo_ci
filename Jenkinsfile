pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                git 'https://github.com/<your-username>/demo-ci-app.git'
            }
        }

        stage('Start Server') {
            steps {
                sh '''
                nohup npm start > app.log 2>&1 &
                sleep 3
                '''
            }
        }

        stage('Run Test') {
            steps {
                sh 'pip3 install --break-system-packages selenium pytest >/dev/null'
                sh 'pytest -v test_ui.py'
            }
        }
    }

    post {
        always {
            sh 'pkill node || true'
        }
    }
}