pipeline {
    agent any
    stages 
    {
        stage('Hello') 
        {
            steps 
            {
                echo 'Hello ${Name}'
            }
            
        }
        stage('tesing')
        {
            steps 
            {
               sh '''
               mkdir Sdir
               cd Sdir
               touch t.txt
               echo "hello sandeep" > t.txt
               '''
            }
        }
    }
    post {
        always 
        {
          echo "This block is always running"
        }
        success 
        {
          echo 'This will run only if successful'
        }
        failure
        {
          echo 'This will run only if failed'
        }
        unstable 
        {
          echo 'This will run only if the run was marked as unstable'
        }
    }    
}
