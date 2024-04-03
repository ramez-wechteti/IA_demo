pipeline {
    agent any

    stages {
        stage('GIT') {
            steps {
                git branch: 'main', credentialsId: 'git-ramez', url: 'https://github.com/ramez-wechteti/IA_demo.git'
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
        
        stage('Build docker image') {
            steps {
                script {

                    dir('resources') {
                        sh 'pwd -P'
                    }
                    

                    sh 'cp -r /srv/samba/share/ resources/'
                    sh 'docker build -t ia_detection .'

                    dir('resources') {
                        deleteDir()
                    }
                }
            }
        }
        
        stage('production') {
            steps {
                script {
                    sh 'docker run -d -v /home/Bigda/fai_workspace/prod/python/output:/app/output ia_detection'
                }
            }
        }
    }

}