pipeline {
    agent any

    stages {
        stage('GIT') {
            steps {
                git branch: 'main', credentialsId: 'git-ramez', url: 'https://github.com/mhaddad86/IA_Demo.git'
            }
        }

        stage('Extraction de Git Hash') {
            steps {
                script {
                    def gitHashFull = sh(script: 'git rev-parse --short=7 HEAD', returnStdout: true).trim()
                    currentBuild.displayName = "Build ${gitHashFull} - #${currentBuild.number}"
                    env.GIT_HASH = gitHashFull
                }
            }
        }

        stage('Transfert vers Env-Test') {
            steps {
                script {
                    def currentDate = sh(script: 'date "+%Y%m%d_%H%M%S"', returnStdout: true).trim()
                    def destinationFolder = "/home/Bigda/fai_workspace/uat/python"
                    def dirExists = sh(script: "[ -d '${destinationFolder}' ] && echo 'true' || echo 'false'", returnStdout: true).trim()

                    if (dirExists == 'false') {
                        sh "mkdir -p ${destinationFolder}"
                        echo "Directory created at ${destinationFolder}"
                    }
                    
                    sh "rsync -av --exclude='.gitattributes' --exclude='Jenkinsfile' * ${destinationFolder}/${env.GIT_HASH}_${currentDate}"
                }
            }
        }
    }

}