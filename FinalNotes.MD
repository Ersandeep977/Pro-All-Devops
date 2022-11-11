#  Rrunning all the Ec2 Instances
```
pipeline
{
    agent any
    stages
    {
        stage('tasting')
        {
            steps
            {
            withCredentials([[ 
                $class: 'AmazonWebServicesCredentialsBinding', 
                credentialsId: 'AWS-Jenkins-Ec2-Full-acess', 
                accessKeyVariable: 'AWS_ACCESS_KEY_ID', 
                secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']])
                {
               sh ''' 
                echo "=================Ansible-m-server-Start================================"
                aws ec2 start-instances --instance-ids i-06ca7c07761f468fd  --region us-east-2
                echo "=================Ansible-m-Node-A-Start================================"
                aws ec2 start-instances --instance-ids i-0589b7c12d3ee6928 --region us-east-2
                echo "==================Ansible-Node-B-Start================================="
                aws ec2 start-instances --instance-ids i-0569707a0704abbda --region us-east-2
                echo "===================== All the EC2 instances Now Running================"
                '''
                }
            }
        }
    } 
}    
```
