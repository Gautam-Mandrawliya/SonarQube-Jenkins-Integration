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
			-Dsonar.login=admin \
            -Dsonar.password=Admin@123 \
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
}
