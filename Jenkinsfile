pipeline {
    agent any
    
    tools {
        maven 'Maven 3.8.1' // Name defined in Global Tool Configuration
    }
    
    environment {
        // SonarQube environment variable, replace 'SonarQubeServer' with the actual name of your SonarQube server configured in Jenkins
        SONARQUBE_ENV = 'SonarQubeServer'
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
                // Run tests
                sh 'mvn test'
            }
        }
        
        stage('Code Quality Analysis') {
            steps {
                // Run code quality analysis using SonarQube
                withSonarQubeEnv('SonarQubeServer') { // Replace 'SonarQubeServer' with your actual SonarQube configuration name
                    sh 'mvn sonar:sonar -Dsonar.projectKey=my_project_key -Dsonar.projectName="My Awesome Web Application" -Dsonar.host.url='http://192.168.1.2:9000'
                }
            }
        }
        
        stage('Deploy') {
            steps {
                // Deploy the application (e.g., to a server or a container)
                // You can customize this part based on your deployment strategy
                sh 'mvn deploy'
            }
        }
        
        stage('Release') {
            steps {
                // Release the application, e.g., pushing to a repository
                sh 'mvn release:prepare release:perform'
            }
        }
    }
    
    post {
        success {
            // Actions to perform on success
            echo 'Pipeline completed successfully!'
        }
        failure {
            // Actions to perform on failure
            echo 'Pipeline failed!'
        }
    }
}


