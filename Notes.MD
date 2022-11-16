# Ec2 instance code pipeline code
### some import link
#### 1.Jenkins Pipeline
https://cloudaffaire.com/jenkins-pipeline-part-2-stages-and-steps/
#### 2. try Catch Block
https://syntaxfix.com/question/1236/try-catch-block-in-jenkins-pipeline-script

```
pipeline
{
    agent any
    stages
    {
        stage('Aws Ec2 Running ')
        {
            steps
            {
            withCredentials([[ 
                $class: 'AmazonWebServicesCredentialsBinding', 
                credentialsId: 'AWS-Jenkins-Ec2-Full-acess', 
                accessKeyVariable: 'AWS_ACCESS_KEY_ID', 
                secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']]) {
               // sh "aws ec2 describe-instances --instance-ids i-0569707a0704abbda --region us-east-2"
               //sh "aws ec2 start-instances --instance-ids i-0569707a0704abbda --region us-east-2"
               sh "aws ec2 stop-instances --instance-ids i-0569707a0704abbda --region us-east-2"
                    
                }
            }
        }
    }
}
```
## Start the all ec2 instances
```
// this file are start the all ec2 instances
pipeline
{
    agent any
    stages
    {
        stage('Ansible-m-server-Start')
        {
            steps
            {
            withCredentials([[ 
                $class: 'AmazonWebServicesCredentialsBinding', 
                credentialsId: 'AWS-Jenkins-Ec2-Full-acess', 
                accessKeyVariable: 'AWS_ACCESS_KEY_ID', 
                secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']])
                {
               sh "aws ec2 start-instances --instance-ids i-06ca7c07761f468fd  --region us-east-2"
                }
            }
        }
        stage('Ansible-m-Node-A-Start')
        {
            steps
            {
            withCredentials([[ 
                $class: 'AmazonWebServicesCredentialsBinding', 
                credentialsId: 'AWS-Jenkins-Ec2-Full-acess', 
                accessKeyVariable: 'AWS_ACCESS_KEY_ID', 
                secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']])
                {
               sh "aws ec2 start-instances --instance-ids i-0589b7c12d3ee6928 --region us-east-2"
                }
            }
        }
        stage('Ansible-Node-B-Start')
        {
            steps
            {
            withCredentials([[ 
                $class: 'AmazonWebServicesCredentialsBinding', 
                credentialsId: 'AWS-Jenkins-Ec2-Full-acess', 
                accessKeyVariable: 'AWS_ACCESS_KEY_ID', 
                secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']])
                {
               sh "aws ec2 start-instances --instance-ids i-0569707a0704abbda --region us-east-2"
                }
            }
        }
    }
}
```
## Pem key using pipeline
```
pipeline
{
    agent any
    stages
    {
        stage('Aws Ec2 Running ')
        {
            steps
            {
            sshagent(['Aws-Jenkins-Pem-key']) 
            {
            sh "ssh  -o  StrictHostKeyChecking=no ec2-user@18.218.228.56 ls"
            }
            }
        }
    }
}
```
