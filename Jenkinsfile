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