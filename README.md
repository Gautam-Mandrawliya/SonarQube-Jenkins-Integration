# SonarQube-Jenkins-Integration

# Test-App for Manual Testing

## Overview

Test-App is a Java application designed to demonstrate code quality analysis using SonarQube.

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- Java (version 11 or higher)
- [SonarQube](https://www.sonarqube.org/downloads/) server running
- [SonarScanner](https://docs.sonarqube.org/latest/analysis/scan/sonarscanner/) installed
- Apache Maven

## Getting Started

1. Create Build using "pom.xml.bkp" and "sonar-project.properties":

   ```bash
   mvn clean install
   
  sonar-scanner \
  -Dsonar.projectKey=Test-App \
  -Dsonar.sources=src/main/java \
  -Dsonar.tests=src/test/java \
  -Dsonar.java.binaries=target/classes \
  -Dsonar.host.url=http://13.201.119.10:9000 \
  -Dsonar.login=squ_1c7e965b714e9bb1ed601e6be5ed8d4a2aee94ea
