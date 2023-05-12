Instructions
============

In any programming language you prefer, write a program that is able to list the Pods on a certain cluster with the following arguments:

```python
--namespace <NAMESPACE> - will show the only Pods from the given namespace
--node <NODE> - will show only the Pods from a given node
```
For example: `kubeget –node some-node-name` will show the Pods only from the some-node-name
The program should be able to run without any arguments, simply by executing ‘kubeget’
The output, regardless of what argument is used, should look like this:

```python
POD NAME                        Number of Labels     Node Name            NAMESPACE
=========                       ==============       ==========           ===========

<POD_NAME>                      <NUM_OF_LABELS>      <NODE_NAME>          <NAMESPACE>
<ACTUAL_POD_NAME>               <NUM_OF_LABELS>      <NODE_NAME>          <NAMESPACE>

```

The program should be able to manage the following scenarios regarding cluster 
context:
- Use current Kubernetes context if it exists
- If no Kubernetes context is currently set, display clear message of telling the user no context is set

