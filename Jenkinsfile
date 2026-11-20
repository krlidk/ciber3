pipeline {
    agent any

    stages {
        stage('Construcción') {
            steps {
                echo 'Construyendo la imagen Docker de la aplicación...'
                sh 'docker build -t app-securedev:latest .'
            }
        }

        stage('Pruebas') {
            steps {
                echo 'Ejecutando pruebas unitarias...'
                sh 'pytest'
            }
        }

        stage('Despliegue') {
            steps {
                echo 'Desplegando contenedor en puerto 5000...'
                sh 'docker rm -f app-securedev-prod || true'
                sh 'docker run -d --name app-securedev-prod -p 5000:5000 app-securedev:latest'
            }
        }
    }
}