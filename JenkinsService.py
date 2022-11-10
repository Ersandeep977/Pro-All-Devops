
import jenkins

j = jenkins.Jenkins('http://192.168.56.1:8080', username='admin', password='root')

# print the user and jenking version
user = j.get_whoami()
version = j.get_version()
#print('Hello %s from Jenkins %s' % (user['fullName'], version))


# print the jobs count number 
Total_Count = j.jobs_count()

def JenkinsInfo():
    print('*'*80)
    print('*'*24,'Print the Jenkins Information','*'*24)
    print('*'*80)
    print('[1].Jenkins User Name ===>',user['fullName'])
    print('[2].Jenkins version ===>',version)
    print('[3].Total Number of the Jenkins job Running ===>',Total_Count)
    print('*'*80)
    

    