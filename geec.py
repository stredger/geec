
import argparse
import requests
import sys
import os
import json

# read request from command line args
# 
#
#

urls = {'newjob': '/job/new',
        'job': '/job/',
        'queue': '/queue/'}



MASTER_SERVER = 'localhost:3000'


def joinurl(base, tojoin):
    pass


def post_request(host, data, headers):
    return requests.post(host, data=data, headers=headers)


def new_job(username, key, jobname, jobfile):
    url = 'http://' + MASTER_SERVER + urls['newjob']
    data = {'user':username, 'key':key, 'data':jobfile, 'name':jobname}
    headers = {'content-type':'application/json'}
    return post_request(url, data=json.dumps(data), headers=headers)

def job_status(username, key, jobname):
    url = 'http://' + MASTER_SERVER + urls['job'] + jobname
    data = {'user':username, 'key':key, 'name':jobname}
    headers = {'content-type':'application/json'}
    return post_request(url, data=json.dumps(data), headers=headers)

def queue_status(username, key, queuename=''):
    url = 'http://' + MASTER_SERVER + urls['queue'] + queuename
    data = {'user':username, 'key':key, 'queue':queuename}
    headers = {'content-type':'application/json'}
    return post_request(url, data=json.dumps(data), headers=headers)



def main():
    #new_job('cool-prog', 'coolman', 'stuff')
    queue_status('butts', 'bigbutt')


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Geec: GEE Command Line Interface')
    parser.add_argument('user', metavar='user', help='Gee username')
    parser.add_argument('key', metavar='key', help='Gee key')
    parser.add_argument('cmd', metavar='cmd', help='Command to run')
    parser.parse_args()
    
    # parser.parse_args(sys.argv[1:])
    #main()
