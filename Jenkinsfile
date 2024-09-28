pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                    // Clean and build the project, creating a JAR file
                    sh 'mvn clean package'
                }
            }
        }
        stage('Archive Artifacts') {
            steps {
                // Archive the built JAR file for later use
                archiveArtifacts artifacts: '**/target/*.jar', allowEmptyArchive: true
            }
        }
        stage('Test') {
            steps {
                script {
                    // Run your tests here
                    sh 'mvn test'
                }
            }
        }
        stage('Code Quality Analysis') {
            steps {
                script {
                    // Run SonarQube analysis (assuming you have configured SonarQube)
                    sh 'sonar-scanner'
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    // Deploy your application (assuming a server is available)
                    // This is a placeholder for your actual deployment command
                    echo 'Deploying the application...'
                    // Example: scp target/yourapp.jar user@server:/path/to/deploy
                }
            }
        }
        stage('Release') {
            steps {
                script {
                    // Handle the release process here
                    echo 'Application released successfully!'
                }
            }
        }
    }
}



