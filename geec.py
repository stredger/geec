
import argparse
import requests
import sys
import os
import json

# read request from command line args
#
#
#

class MalformedRequestException(Exception): pass


urls = {'newjob'    : '/job/new',
        'job'       : '/job/',
        'output'    : '/job/output/',
        'queue'     : '/queue/'}



MASTER_SERVER = 'localhost:3000'


def create_http_url(host, *args):
    if '/' in host: raise MalformedRequestException('Bad Host: %s' % (host))
    resource = ''.join(args)
    return 'http://' + host + resource


def post_request(host, data, headers):
    return requests.post(host, data=data, headers=headers)

def get_request(host, data, headers):
    return requests.get(host, data=data, headers=headers)


def new_job(username, key, jobname, jobfile):
    url = create_http_url(MASTER_SERVER, urls['newjob'])
    with open (jobfile, "r") as myfile:
        data = {'user':username, 'key':key, 'data':myfile.read(), 'name':jobname}
    headers = {'content-type':'application/json'}
    return post_request(url, data=json.dumps(data), headers=headers)

def job_output(username, key, jobname):
    url = create_http_url(MASTER_SERVER, urls['output'], jobname)
    data = {'user':username, 'key':key, 'name':jobname}
    headers = {'content-type':'application/json'}
    r = get_request(url, data=json.dumps(data), headers=headers)

    print r.text

def job_status(username, key, jobname):
    url = create_http_url(MASTER_SERVER, urls['job'], jobname)
    data = {'user':username, 'key':key, 'name':jobname}
    headers = {'content-type':'application/json'}
    return post_request(url, data=json.dumps(data), headers=headers)

def queue_status(username, key, queuename=''):
    url = create_http_url(MASTER_SERVER, urls['queue'], queuename)
    data = {'user':username, 'key':key, 'queue':queuename}
    headers = {'content-type':'application/json'}
    return post_request(url, data=json.dumps(data), headers=headers)



if __name__ == "__main__":
    try:
        user = sys.argv[1]
        key = sys.argv[2]
        cmdlist = {'queuestat':queue_status, 'jobstat':job_status, 'free':queue_status, 'new':new_job, 'output': job_output}
        cmd = cmdlist[sys.argv[3]]
        args = sys.argv[4:]
        cmd(user, key, *args)
    except (IndexError, KeyError), e:
        print 'geec.py <user> <key> <cmd> <args>'
        print ' where <cmd> is: queuestat <queuename>'
        print '                 jobstat <jobname>'
        print '                 free'
        print '                 new <jobname> <jobfile>'