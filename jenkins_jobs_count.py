import jenkins
from jenkinsapi import api
#jenkins = api.Jenkins('http://34.250.36.25/jenkins', username='HeckaThon', password='Ready2work')
#awesome_job = jenkins.get_job('echo_hello')
#awesome_build = awesome_job.get_last_build()
#if awesome_build.is_good():
#    print "The build passed successfully"
#else:
#    print awesome_build.get_status()






server = jenkins.Jenkins('http://34.250.36.25/jenkins', username='HeckaThon', password='Ready2work')
#jobs = server.get_jobs()
#print jobs
server.build_job('echo_hello')
