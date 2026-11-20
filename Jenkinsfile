pipeline {
    agent any

    stages {
        stage('Construcción') {
            steps {
                echo 'Construyendo la imagen Docker de la aplicación...'
                bat 'docker build -t app-securedev:latest .'
            }
        }

        stage('Pruebas') {
            steps {
                echo 'Ejecutando pruebas unitarias...'
                bat 'docker run --rm app-securedev:latest pytest'
            }
        }

        stage('Despliegue') {
            steps {
                echo 'Desplegando contenedor en puerto 5000...'
                bat 'docker rm -f app-securedev-prod || ver > nul'
                bat 'docker run -d --name app-securedev-prod -p 5000:5000 app-securedev:latest'
            }
        }
    }
}