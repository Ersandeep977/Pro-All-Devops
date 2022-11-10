# Ec2 instance code
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
