Copy docker-compose.yml to kompose subderictory, then run:
> kompose convert

Start kubernetes cluster:
> minikube start

Check your X(e.g. pod, deployment, svc, replicaset):
> kubectl get X

Dashboard:
> minikube dashboard

Configure environment to use minikube’s Docker daemon. Then when you build some images locally they will be visible to minikube, so in the end you don't have to push everything to hub.
> minikube docker-env

Deployment:
> kubectl apply -f .

Stop:
> minikube stop

Delete:
> minikube delete --all