pipeline {
    agent any // Use 'any' if you're unsure about the environment

    stages {
        stage('Build') {
            agent {
                docker {
                    image 'docker:latest' // Use the Docker image
                    args '-v /var/run/docker.sock:/var/run/docker.sock' // Mount Docker socket
                }
            }
            steps {
                script {
                    // Build your Docker image
                    sh 'docker build -t smart-traffic-signal .'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Run your tests here
                    sh 'pytest tests/'
                }
            }
        }
        stage('Code Quality Analysis') {
            steps {
                script {
                    // Run SonarQube analysis
                    sh 'sonar-scanner'
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    // Deploy your application
                    sh 'docker run -d -p 8080:8080 smart-traffic-signal'
                }
            }
        }
        stage('Release') {
            steps {
                script {
                    // Handle the release process here
                    echo 'Application released!'
                }
            }
        }
    }
}


