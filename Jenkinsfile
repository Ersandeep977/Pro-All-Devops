def VcredentialsId = "credentialsId: 'AWS-Jenkins-Ec2-Full-acess'"
def VaccessKeyVariable = "accessKeyVariable: 'AWS_ACCESS_KEY_ID'"
def VsecretKeyVariable = "secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'"

pipeline
{
    agent any
    stages
    {
        stage('fast')
        {
            steps
            {
            withCredentials([[ 
                $class: 'AmazonWebServicesCredentialsBinding',
                ${VcredentialsId},
                ${VaccessKeyVariable},
                ${VsecretKeyVariable} 
                ]])
                {
               sh ''' 
                echo "=================Ansible-m-server-Start================================"
                aws ec2 start-instances --instance-ids i-06ca7c07761f468fd  --region us-east-2
                '''
                }
            }
        }
       
    } 
}       


// Define variable
def myVariable = "foo"

// Print variable
pipeline {
  agent any
  stages {
    stage ("Print variable") {
      steps {
        echo "My variable is ${myVariable}"
      }
    }
  }
}