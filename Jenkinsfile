pipeline {
    agent any

    stages {

        stage('Create Virtual Environment') {
            steps {
                sh '''
                python3.11 -m venv venv
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                source venv/bin/activate
                python --version
                pip --version
                python -m pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Verify Application') {
            steps {
                sh '''
                source venv/bin/activate
                python -m py_compile backend/web_app.py
                '''
            }
        }
    }
}

