# SonarQube-Jenkins-Integration

## Overview

Java application designed to demonstrate code quality analysis using SonarQube.

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- Java (version 11 or higher)
- [SonarQube](https://www.sonarqube.org/downloads/)
- [SonarScanner](https://docs.sonarqube.org/latest/analysis/scan/sonarscanner/)
- Apache Maven
- Jenkins for Pipeline ("pom.xml", and "Jenkinsfile")

## Test-App for Manual Testing

1. Create Build using "pom.xml.bkp" and "sonar-project.properties":

   ```bash
   mvn clean install -f pom.xml.bkp

   sonar-scanner \
   -Dsonar.projectKey=Test-App \
   -Dsonar.sources=src/main/java \
   -Dsonar.tests=src/test/java \
   -Dsonar.java.binaries=target/classes \
   -Dsonar.host.url=http://13.201.119.10:9000 \
   -Dsonar.login=squ_1c7e965b714e9bb1ed601e6be5ed8d4a2aee94ea

Where as

-Dsonar.projectKey=Test-App: This sets the project key in SonarQube. It should be unique to your project.

-Dsonar.sources=src/main/java: Points to your Java source code directory.

-Dsonar.tests=src/test/java: Points to your test directory (e.g., JUnit tests).

-Dsonar.java.binaries=target/classes: Points to the compiled .class files generated by Maven during the build.

-Dsonar.host.url=http://13.201.119.10:9000: The URL of the SonarQube server where the analysis will be sent.

-Dsonar.login=squ_1c7e965b714e9bb1ed601e6be5ed8d4a2aee94ea: The token used to authenticate the project scan with SonarQube.
   
