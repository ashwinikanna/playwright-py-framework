pipeline {
  agent any
  stages {
    stage('Checkout') { steps { checkout scm } }

    stage('Install + Run') {
      steps {
        sh '''
          python3 -m venv .venv
          . .venv/bin/activate
          pip install -U pip
          pip install -r requirements.txt
          python -m playwright install
          pytest -q
        '''
      }
    }
  }
}
