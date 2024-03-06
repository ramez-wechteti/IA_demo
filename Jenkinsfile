pipeline {
    agent any

    stages {
        stage('GIT') {
            steps {
                git branch: 'main', credentialsId: 'git-ramez', url: 'https://github.com/mhaddad86/IA_Demo.git'
            }
        }
    }

}