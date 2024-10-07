node {
    stage('Cloning from GIT') {
        git branch: 'main', credentialsId: 'GITHUB_CREDS', url: 'https://github.com/Gautam-Mandrawliya/SonarQube-Jenkins-Integration.git'
    }

    stage('SonarQube Analysis') {
        def scannerHome = tool 'SonarQube'
        withSonarQubeEnv('SonarQube') {
            sh """
            ${scannerHome}/bin/sonar-scanner \
            -Dsonar.projectVersion=1.0-SNAPSHOT \
            -Dsonar.login=admin \
            -Dsonar.password=Admin@123 \
            -Dsonar.projectBaseDir=/var/lib/jenkins/workspace/SonarQube-Test/ \
            -Dsonar.projectKey=my-app \
            -Dsonar.sourceEncoding=UTF-8 \
            -Dsonar.language=java \
            -Dsonar.sources=my-app/src/main \
            -Dsonar.tests=my-app/src/test \
            -Dsonar.host.url=http://172.31.34.52:9000/
            """
        }
    }
}
