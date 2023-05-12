
# KUBEGET v.0.9.5. This program list the pods on the K8s cluster. 
# Commandline options:
# --node [nodename]       - show only the Pods from a given node
# --namespace [NAMESPACE] - show the only Pods from the given namespace
# --help -h option for help
#
# Denis Chertkov, denis@chertkov.info, 12/05/2023

import argparse
import json
import subprocess
import sys


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-ns', '--namespace', type=str)
    parser.add_argument('-nn', '--node', type=str)
    return parser

# Will check if kubectl tool is installed
def kubectlIsInstalled():
    try:
        subprocess.call(['kubectl', 'version'],
                        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except:
        return False

# Will check if context is defined
def contextIsDefined():
    try:
        subprocess.check_output(
            ['kubectl', 'config', 'current-context'], universal_newlines=True)
        return True
    except:
        return False

def showPods(namespace, nodename):
    try:
        stdout_string = subprocess.check_output(
            ['kubectl', 'get', 'pod', '--all-namespaces', '-o', 'json'], universal_newlines=True)
    except:
        print('error: Can\'t get the pods from the cluster')
        exit(1)
    
    stdout_struct = json.loads(stdout_string)

    # Fill the pods structure
    pods = []
    for pod in stdout_struct['items']:
        # Do we need to add the current pod to the list?
        list_pod = False
        if namespace == None:                                                       # if namespace not defined
            if nodename == None:                                                    # if namespace AND node not defined
                list_pod = True
            # if namespace defined AND node not defined
            else:
                if nodename == pod['spec']['nodeName']:
                    list_pod = True
        else:                                                                       # if namespace is defined
            # if namespace is defined AND node not defined
            if nodename == None:
                if namespace == pod['metadata']['namespace']:
                    list_pod = True
            # namespace is defined AND nodename also defined
            else:
                if (namespace == pod['metadata']['namespace'] and nodename == pod['spec']['nodeName']):
                    list_pod = True
        if list_pod:
            pods.append({'name': pod['metadata']['name'],                           # Pod name
                        'namespace': pod['metadata']['namespace'],                  # Namespace
                        'nodename': pod['spec']['nodeName'],                        # NodeName
                        'labels': len(pod['metadata']['labels']),                   # Amounts of labels
                        })

    # Show the pods
    print('POD NAME                                         Number of Labels   Node Name                                        NAMESPACE')
    print('=========                                        ================   ==========                                       ===========')
    
    # List the pods
    for pod in pods:
        out_line = '{0:49}{1:<19d}{2:49}{3:27}'.format(
            pod['name'][:48], pod['labels'], pod['nodename'][:48], pod['namespace'][:26])
        print(out_line)
    # print('=========                                        ================   ==========                                ===========')
    # print('POD NAME                                         Number of Labels   Node Name                                 NAMESPACE')

if __name__ == '__main__':

    print("KUBEGET v.0.9.5. This program list the pods on the K8s cluster. Run with -h option for help.")
    print("Denis Chertkov, denis@chertkov.info, 12/05/2023")

    if not kubectlIsInstalled():
        print('error: The kubectl CLI tool is not installed. Please istall it first.')
        exit(1)

    if not contextIsDefined():
        print('error: Please set the current context first.')
        exit(1)

    # Parse the commandline. If no parameters are specified, use the default values None
    parser = createParser()
    args = parser.parse_args(sys.argv[1:])
    namespace = args.namespace
    nodename = args.node

    # Show selected pods
    showPods(namespace=namespace, nodename=nodename)

    exit(0)
