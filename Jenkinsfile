pipeline {
    agent { label 'jenkins-example' }
    environment {
        ALLURE_RESULT_PATH = './allure'
    }
    stages {
        stage('Prepare Test Environment') {
            steps {
                sh '''
                    echo "Install dependencies"
                    echo ${ALLURE_RESULT_PATH}
                    pipenv install
                '''
            }
        }
        stage('Execute Automation Tests') {
            steps {
                sh 'pipenv run test_all || true'
            }
        }
        stage('Generate Allure Report') {
            steps {
                sh 'pipenv run generate_allure_report'
            }
        }
    }
}
