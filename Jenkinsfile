pipeline {
    agent { label 'agent' }

    environment {
        DOCKER_IMAGE_OWNER = 'bamyam'
    }

    stages {
        stage('init') {
            steps {
                sh 'rm -rf *'
            }
        }
        stage('Checkout') {
            steps {
                sh '''
                git clone https://github.com/bamyam/hellomsa.git
                '''
            }
        }

        stage('Docker Image Build') {
            steps {
                echo "${env.Build_number}"
                sh """
                cd hellomsa
                docker build -t ${DOCKER_IMAGE_OWNER}/frontendapp:v${env.Build_number} ./msa-frontend
                docker build -t ${DOCKER_IMAGE_OWNER}/productapp:v${env.Build_number} ./product-service
                docker build -t ${DOCKER_IMAGE_OWNER}/userapp:v${env.Build_number} ./user-service
                """
            }
        }

        stage('Docker Image Push') {
            steps {
                withDockerRegistry([credentialsId: 'docker-hub-login', url: ""]) {
                    sh """
                    docker push ${DOCKER_IMAGE_OWNER}/frontendapp:v${env.Build_number}
                    docker push ${DOCKER_IMAGE_OWNER}/productapp:v${env.Build_number}
                    docker push ${DOCKER_IMAGE_OWNER}/userapp:v${env.Build_number}
                    """
                }
            }
        }
        stage('Checkout2') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'github-login', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    sh '''
                    git clone https://github.com/bamyam/hellomsaips-main.git
                    ls hellomsaips-main
                    '''
                }
            }
        }
        stage('convert chart') {
            steps {
                sh """
                cd hellomsaips-main
                sed -i "s/v[0-9]\\+/v${env.Build_number}/g" hellomsa-prd/values.yaml
                """
            }
        }
        stage('hellomsaips-main push'){
            steps {
                withCredentials([usernamePassword(credentialsId: 'github-login', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                sh '''
                cd /home/jenkins/workspace/hellomsa/hellomsaips-main
                git config --global user.email "seoseungjae20209@gmail.com"
                git config --global user.name "bamyam"
                git add hellomsa-prd/values.yaml
                git commit -m "hello gitopsB commit"
                git push https://"${USERNAME}":"${PASSWORD}"@github.com/bamyam/hellomsaips-main.git HEAD:main
                '''
                }
            }
        }
    }

}
