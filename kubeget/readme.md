Instructions
============

In any programming language you prefer, write a program that is able to list the Pods on a certain cluster with the following arguments:

```
--namespace <NAMESPACE> - will show the only Pods from the given namespace
--node <NODE> - will show only the Pods from a given node
```
For example: `kubeget --node some-node-name` will show the Pods only from the some-node-name
The program should be able to run without any arguments, simply by executing ‘kubeget’
The output, regardless of what argument is used, should look like this:

```
POD NAME                        Number of Labels     Node Name            NAMESPACE
=========                       ==============       ==========           ===========

<POD_NAME>                      <NUM_OF_LABELS>      <NODE_NAME>          <NAMESPACE>
<ACTUAL_POD_NAME>               <NUM_OF_LABELS>      <NODE_NAME>          <NAMESPACE>
```

The program should be able to manage the following scenarios regarding cluster 
context:
- Use current Kubernetes context if it exists
- If no Kubernetes context is currently set, display clear message of telling the user no context is set

Solution
============

The program is written in Python 3. No additional libraries are required. 

The options can be used one at a time or combined. In case of both options will use (--namespace and --node), pods satisfying both conditions will be shown. With -h option, help is shown:
```$ python3 kubeget.py -h
KUBEGET v.0.9. This program list the pods on the K8s cluster. Run with -h option for help.
Denis Chertkov, denis@chertkov.info, 12/05/2023
usage: kubeget.py [-h] [-ns NAMESPACE] [-nn NODE]

optional arguments:
  -h, --help            show this help message and exit
  -ns NAMESPACE, --namespace NAMESPACE
  -nn NODE, --node NODE
  ```
The program uses the cubelet CLI. Before you start using the program, please check that your context is defined:
```
$ kubectl config current-context
test12
```
The program has a limit on the length of the name pods and nodes - no more than 48 characters. Sometimes it can be significant.