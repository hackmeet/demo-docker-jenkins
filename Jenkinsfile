pipeline {
    agent any

    stages {
         stage('add env') {
            steps {
                echo 'setting env path'
                sh 'export PATH=$PATH:/usr/bin'
                echo "after pulling code"
            }
        }
        stage('SCM') {
            steps {
                echo 'pulling code from scm'
                git branch: 'main', url: 'https://github.com/hackmeet/demo-docker-jenkins.git'
                echo "after pulling code"
            }
        }
        stage('build docker image') {
            steps {
                echo 'building the docker image'
                sh 'docker image build -t meetvasani/python-server .'
            }
        }
        stage('docker login') {
            steps {
                echo 'llogging in docker hub'
                withCredentials([string(credentialsId: 'DOCKER_HUB_TOKEN', variable: 'DOCKER_HUB_TOKEN')]) {
                    sh 'echo $DOCKER_HUB_TOKEN | docker login -u meetvasani --password-stdin'
                }
            }
        }
        stage('docker push image') {
            steps {
                echo 'pushing to docker hub'
                sh 'docker image push meetvasani/python-server'
            }
        }
        stage('remove docker service') {
            steps {
                echo 'removing exiting docker service'
                sh 'docker service rm python-server'
            }
        }
        stage('create new docker service') {
            steps {
                echo 'creating new docker service'
                sh 'docker service create --name python-server -p 5000:5000 --replicas 5 meetvasani/python-server'
            }
        }
    }
}
