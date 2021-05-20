Prerequisites: installed minikube

Start kubernetes cluster:
> minikube start

Check your X(e.g. pod, deployment, svc, replicaset):
> kubectl get X

Dashboard:
> minikube dashboard

Configure environment to use minikube’s Docker daemon. Follow instruction it will print at the end. 
Then when you will build docker images using the terminal you set it up(e.g by docker compose up)
the images will use minikube's docker, and they will be visible to minikube when deploying kubernetes.
We won't need this after we start pushing images to docker hub repository.
> minikube docker-env

Accessing apps, make sure they have external IP defined:
> minikube tunnel

Deployment(from ./kubernetes/deploy):
> kubectl apply -f .

Stop:
> minikube stop

Delete(purge, it will delete entire container including all images made inside of it locally):
> minikube delete --all
