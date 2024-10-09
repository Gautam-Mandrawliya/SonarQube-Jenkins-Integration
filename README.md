# SonarQube-Jenkins-Integration

## Manual Testing using "pom.xml.bkp" and "sonar-project.properties"
```bash
sonar-scanner \
-Dsonar.projectKey=Test-App \
-Dsonar.sources=src/main/java \
-Dsonar.tests=src/test/java \
-Dsonar.java.binaries=target/classes \
-Dsonar.host.url=http://13.201.119.10:9000 \
-Dsonar.login=squ_1c7e965b714e9bb1ed601e6be5ed8d4a2aee94ea
