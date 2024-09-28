pipeline {
    agent any
    
    tools {
        maven 'Maven 3.8.1' // Name defined in Global Tool Configuration
    }
    
    environment {
        SONARQUBE_ENV = 'SonarQubeServer' // Your SonarQube configuration name
    }
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout code from GitHub
                git branch: 'main', url: 'https://github.com/shreydsaraf/Project.git'
            }
        }
        
        stage('Build') {
            steps {
                // Build the project and create a JAR file
                sh 'mvn clean package'
            }
        }
        
        stage('Archive Artifacts') {
            steps {
                // Archive the JAR file created during the build stage
                archiveArtifacts artifacts: 'target/*.jar', fingerprint: true
            }
        }
        
        stage('Test') {
            steps {
                // Run tests with JUnit
                sh 'mvn test'
            }
        }
        
        stage('Code Quality Analysis') {
            steps {
                // Run code quality analysis using SonarQube
                withSonarQubeEnv('SonarQubeServer') {
                    sh 'mvn sonar:sonar -Dsonar.projectKey=my_project_key -Dsonar.projectName="My Awesome Web Application" -Dsonar.host.url=http://192.168.1.2:9000'
                }
            }
        }
        
        stage('Deploy') {
            steps {
                // Deploy the application (e.g., to a server or a container)
                // Customize based on your deployment strategy
                sh 'mvn deploy'
            }
        }
        
        stage('Monitoring and Alerting') {
            steps {
                echo 'Monitoring and Alerting stage executed (placeholder).'
            }
        }
        
        stage('Release') {
            steps {
                echo 'Release stage executed (placeholder).'
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}



