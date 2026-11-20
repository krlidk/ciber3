pipeline {
    agent any

    stages {
        stage('Construcción') {
            steps {
                echo 'Construyendo imagen Docker...'
                bat 'docker build -t app-securedev:latest .'
            }
        }

        stage('Revisión SAST (Bandit)') {
            steps {
                echo 'Ejecutando análisis estático de seguridad en el código...'
                bat 'docker run --rm app-securedev:latest bandit -r app.py'
            }
        }

        stage('Auditoría de Dependencias (SCA)') {
            steps {
                echo 'Verificando vulnerabilidades conocidas en librerías...'
                bat 'docker run --rm app-securedev:latest pip-audit'
            }
        }

        stage('Pruebas Unitarias y de Seguridad') {
            steps {
                echo 'Ejecutando pruebas funcionales y anti-XSS...'
                bat 'docker run --rm app-securedev:latest pytest'
            }
        }

        stage('Pruebas DAST (OWASP ZAP)') {
            steps {
                echo 'Iniciando entorno temporal y escaneo dinámico con OWASP ZAP...'
                bat '''
                    docker network create zap-net || ver > nul
                    docker rm -f app-securedev-test || ver > nul
                    docker run -d --name app-securedev-test --network zap-net app-securedev:latest
                    ping -n 6 127.0.0.1 > nul
                    docker run --rm --network zap-net -v "%WORKSPACE%:/zap/wrk/:rw" ghcr.io/zaproxy/zaproxy:stable zap-baseline.py -t http://app-securedev-test:5000/hello?name=test -r zap_report.html || ver > nul
                    docker rm -f app-securedev-test || ver > nul
                '''
            }
        }

        stage('Despliegue') {
            steps {
                echo 'Desplegando aplicación segura en puerto 5000...'
                bat 'docker rm -f app-securedev-prod || ver > nul'
                bat 'docker run -d --name app-securedev-prod -p 5000:5000 app-securedev:latest'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'zap_report.html', allowEmptyArchive: true
        }
    }
}