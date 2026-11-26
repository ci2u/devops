# Learning roadmap — AKS DevOps lab

## ✅ Step 0 – Workstation setup
WSL2 Ubuntu 24.04, VS Code + WSL extension, Docker Desktop, git, gh, az, terraform

## ✅ Step 1 – Minimal web app (Python/Flask)
- `/` endpoint with GREETING env var and hostname
- `/healthz` health endpoint
- Shell variable vs environment variable (`export`)
- Challenge: `/version` endpoint reading APP_VERSION

## ✅ Step 2 – Dockerfile
- gunicorn as production server
- Layer caching (requirements before code), .dockerignore
- Build args (ARG) vs runtime env (ENV)
- docker build / run / ps / logs / exec
- Challenge: run as non-root user (uid 10001)

## ✅ Step 3 – Docker Compose
- Two services: app + Redis (visit counter)
- Service discovery by name, depends_on + service_healthy
- Named volume (data survives `down`)
- Graceful degradation when Redis is down
- Challenge: app healthcheck (urllib)

## ✅ Step 4 – Kubernetes on my laptop (Docker Desktop)
- 4.1 Check the local cluster
- 4.2 First Pod (imperative) – and why Pods alone are not enough
- 4.3 Namespace, Deployment, Service as YAML (declarative)
- 4.4 Explore: get / describe / logs / exec / port-forward
- 4.5 Self-healing and scaling
- 4.6 Load balancing and cluster DNS
- 4.7 Rolling update and rollback
- 4.8 ConfigMap for configuration
- Challenge: break the liveness probe, watch Kubernetes restart the container

## ⬜ Step 5 – Terraform: Azure resource group + Container Registry
Push my image to ACR (cost: a few cents)

## ⬜ Step 6 – Terraform: AKS
Deploy to AKS, LoadBalancer with public IP, collect evidence, `terraform destroy`

## ⬜ Step 7 – CI with GitHub Actions
Lint + tests, docker build, smoke test, image scan, terraform validate

## ⬜ Step 8 – CD with GitHub Actions + OIDC
Passwordless deploy to AKS, least-privilege roles

## ⬜ Step 9 – Documentation
README, architecture diagram, cost notes, lab journal, screenshots

## Optional extras (when time allows)
- Multi-stage Dockerfile, read-only filesystem
- HPA autoscaling, PodDisruptionBudget, NetworkPolicy, Pod Security "restricted"
- Kustomize or Helm
- Redis in Kubernetes (StatefulSet / PVC)
