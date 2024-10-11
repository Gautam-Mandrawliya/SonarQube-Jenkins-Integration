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
            -Dsonar.projectBaseDir=/var/lib/jenkins/workspace/Sonar-Pipeline/ \
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
	
	// Generate CSV report using SonarQube API
    stage('Generate SonarQube Report') {
        sh '''
			pip3 install requests urllib3<2.0
	#		pip3 install requests
			python3 generate_sonar_report.py
		'''
    }
    
    // Archive the report as a build artifact
    stage('Archive Report') {
        archiveArtifacts artifacts: 'sonarqube_report.csv'
    }
}

