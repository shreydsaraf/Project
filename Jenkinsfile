pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // Checkout code from SCM
                git 'https://github.com/shreydsaraf/Project.git'
            }
        }
        stage('Build') {
            steps {
                // Use Maven to build the project
                sh 'mvn clean package'
            }
        }
        stage('Archive Artifacts') {
            steps {
                // Archive the built JAR file
                archiveArtifacts artifacts: '**/target/*.jar', fingerprint: true
            }
        }
        stage('Test') {
            steps {
                // Run your tests here
                sh 'mvn test'
            }
        }
        stage('Code Quality Analysis') {
            steps {
                // Run SonarQube analysis or any other tool
                sh 'mvn sonar:sonar'
            }
        }
        stage('Deploy') {
            steps {
                // Deploy your application if needed
                echo 'Deploying application...'
            }
        }
        stage('Release') {
            steps {
                // Handle the release process here
                echo 'Application released!'
            }
        }
    }
}



