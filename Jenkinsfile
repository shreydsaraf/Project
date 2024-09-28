pipeline {
    agent {
        docker {
            image 'docker:latest'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
    stages {
        stage('Build') {
            steps {
                script {
                    sh 'docker build -t smart-traffic-signal .'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Run your tests here, ensure you have pytest installed in your image
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
                    // Deploy your application, you might want to specify ports or other options
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

