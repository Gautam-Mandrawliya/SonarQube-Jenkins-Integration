import groovy.json.JsonSlurper
import java.util.Base64

node {
    stage('Cloning from GIT') {
        git branch: 'main', credentialsId: 'GITHUB_CREDS', url: 'https://github.com/Gautam-Mandrawliya/SonarQube-Jenkins-Integration.git'
    }
    
    stage('Build') {
        def mvnHome = tool 'Maven'  
        sh "${mvnHome}/bin/mvn clean install"
    }
    
    stage('SonarQube Analysis') {
        def scannerHome = tool 'SonarQube'
        withSonarQubeEnv('SonarQube') {
            sh """
            ${scannerHome}/bin/sonar-scanner \
            -Dsonar.projectVersion=1.0-SNAPSHOT \
            -Dsonar.login=squ_1c7e965b714e9bb1ed601e6be5ed8d4a2aee94ea \
            -Dsonar.projectBaseDir=${env.WORKSPACE} \
            -Dsonar.projectKey=my-app \
            -Dsonar.sourceEncoding=UTF-8 \
            -Dsonar.language=java \
            -Dsonar.sources=src/main/java \
            -Dsonar.tests=src/test/java \
            -Dsonar.host.url=http://172.31.34.52:9000/ \
            -Dsonar.java.libraries=target/classes,target/test-classes
            """
        }
    }
    
    stage('Fetch SonarQube Report') {
        script {
            def sonarHost = "http://172.31.34.52:9000"
            def projectKey = "my-app"
            def authToken = "squ_1c7e965b714e9bb1ed601e6be5ed8d4a2aee94ea"

            // Base64 encode the authentication token
            String encodedAuthToken = Base64.getEncoder().encodeToString(authToken.getBytes())

            def sonarUrl = "${sonarHost}/api/issues/search?componentKeys=${projectKey}&resolved=false"
            def sonarResponse = new URL(sonarUrl).getText(requestProperties: ['Authorization': "Basic ${encodedAuthToken}"])
            def json = new JsonSlurper().parseText(sonarResponse)

            // Write data to CSV file
            def reportFile = new File("${env.WORKSPACE}/sonarqube_report.csv")
            reportFile.withWriter { writer ->
                writer.writeLine("Issue Key, Severity, Type, Message, Line")
                
                json.issues.each { issue ->
                    writer.writeLine("${issue.key}, ${issue.severity}, ${issue.type}, ${issue.message}, ${issue.line}")
                }
            }

            // Archive the report for future reference
            archiveArtifacts artifacts: 'sonarqube_report.csv', fingerprint: true
        }
    }
}
