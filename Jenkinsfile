pipeline {
    agent any

    environment {
        ANSIBLE_HOST_KEY_CHECKING = 'False'
        ANSIBLE_FORCE_COLOR        = 'true'
        APP_VERSION                = "1.${BUILD_NUMBER}.0"
    }

    stages {

        stage('1. Checkout') {
            steps {
                checkout scm
                sh 'ls -la'
            }
        }

        stage('2. Tests unitaires') {
            steps {
                dir('app') {
                    sh '''
                        pip3 install -q flask pytest
                        pytest test_app.py -v
                    '''
                }
            }
        }

        stage('3. Build artefact') {
            steps {
                sh '''
                    mkdir -p artifact
                    tar -czf artifact/app.tar.gz -C app app.py requirements.txt test_app.py
                    ls -lh artifact/
                '''
                archiveArtifacts artifacts: 'artifact/app.tar.gz', fingerprint: true
            }
        }

        stage('4. Lint Ansible') {
            steps {
                dir('ansible') {
                    sh 'ansible-playbook site.yml --syntax-check'
                }
            }
        }

        stage('5. Deploy Rolling') {
            steps {
                dir('ansible') {
                    sh """
                        ansible-playbook -i inventory.ini site.yml \
                          -e "app_version=${APP_VERSION}"
                    """
                }
            }
        }

        stage('6. Smoke Tests') {
            steps {
                sh '''
                    for target in target1 target2; do
                        echo "=== Test sur $target ==="
                        RESPONSE=$(docker exec $target curl -s http://localhost:5000/health)
                        echo "Réponse: $RESPONSE"
                        echo "$RESPONSE" | grep -q '"status":"ok"' || exit 1
                    done
                    echo "✅ Tous les smoke tests passent"
                '''
            }
        }

        stage('7. Vérification version') {
            steps {
                sh '''
                    for target in target1 target2; do
                        VERSION=$(docker exec $target curl -s http://localhost:5000/ | grep -o '"version":"[^"]*"')
                        echo "$target: $VERSION"
                    done
                '''
            }
        }
    }

    post {
        always {
            echo "🏁 Build #${BUILD_NUMBER} terminé : ${currentBuild.currentResult}"
        }
        success {
            echo "✅ Déploiement v${APP_VERSION} réussi sur target1 + target2"
        }
        failure {
            echo "❌ Build #${BUILD_NUMBER} échoué — voir les logs"
        }
    }
}
