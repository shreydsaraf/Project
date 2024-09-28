pipeline {
    agent any
    
    tools {
        maven 'Maven 3.8.1' // Name defined in Global Tool Configuration
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
                // Run code quality analysis (using tools like SonarQube, if set up)
                // Example using SonarQube
                sh 'mvn sonar:sonar'
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
                // Release the application
                // Example for releasing, e.g., pushing to a repository
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



