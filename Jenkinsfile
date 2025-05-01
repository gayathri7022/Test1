pipeline {
    agent any
        stages {
            stage ('Checkout code'){
                steps {
                    git credentialsId:'MY_PAT', url:"https://github.com/gayathri7022/Test1.git", branch:"main"
                }
            }

            stage ('Install dependencies') {
                steps {
                    bat '''
                        python venv venv -m
                        call venv\\Scripts\\activate
                        pip install --upgrade pip
                        pip install pytest
                    '''
                }
            }

            stage('Test') {
                steps{
                    bat '''
                        call venv\\Scripts\\activate
                        pytest test.py
                    '''
                }
            }

            stage('Deploy') {
                steps{
                    bat '''
                        call venv\\Scripts\\activate
                        python student.py
                    '''
                }
            }
        }
}