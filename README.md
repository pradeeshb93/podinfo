# podinfo
* Install eksctl and create a K8s cluser in aws using below command

``` eksctl create cluster \
    --name eks-from-eksctl \
    --version 1.16 \
    --region us-west-2 \
    --nodegroup-name workers \
    --node-type t3.medium \
    --nodes 1 \
    --nodes-min 1 \
    --nodes-max 2 \
    --ssh-access \
    --ssh-public-key ~/.ssh/eks-demo.pem.pub \
    --managed
    ```
 Configure eksctl and iam authenticator to get access to the cluster. 
 
 App
 
 * application is exposed using nginx and gunicorn. The app.py under app director is used to fetch the pod ip using python k8s client.
 
 Dockerfile
 
 Build the docker images and push it to docker hub.
 
 ``` docker build -t poddata:tag-1 . ```
 
 The image is available in https://hub.docker.com/r/pradeeshb/poddata
 
 
 * Create the k8s objects using kubectl command.
 * Follow the same steps for objects in namespace n2.
 * app will scale based on cpu
 
 Output
 =====
 
 * Get the worker node ip
 
``` kubectl get node -o wide ```
 
 * Edit /etc/hosts and add entry for localhost to worker node ip
 * curl localhost:30080 and curl localhost:30081 to get pod info
 
 
 
 
 


