pipeline {

    agent any

    stages {

        stage('Clone') {
            steps {
                git 'https://github.com/YOUR_USERNAME/AI_sign_language_system.git'
            }
        }

        stage('Create Virtual Environment') {
            steps {
                sh '''
                python3 -m venv venv
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Application') {
            steps {
                sh '''
                . venv/bin/activate
                nohup python backend/web_app.py > flask.log 2>&1 &
                '''
            }
        }

    }
}
