
# Cloud + DevOps + MLOps: Zero to Production

![Linux](https://img.shields.io/badge/Linux-Ubuntu-orange?logo=ubuntu)
![Docker](https://img.shields.io/badge/Docker-Containerization-blue?logo=docker)
![AWS](https://img.shields.io/badge/AWS-Cloud_Engineering-orange?logo=amazonaws)
![Terraform](https://img.shields.io/badge/Terraform-IaC-7B42BC?logo=terraform)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Orchestration-326CE5?logo=kubernetes)
![Jenkins](https://img.shields.io/badge/Jenkins-CI%2FCD-D24939?logo=jenkins)
![Prometheus](https://img.shields.io/badge/Prometheus-Monitoring-E6522C?logo=prometheus)
![Grafana](https://img.shields.io/badge/Grafana-Observability-F46800?logo=grafana)
![Cost](https://img.shields.io/badge/Cloud_Infrastructure_Cost-%240-success)

A structured, hands-on engineering roadmap designed to build practical expertise in Linux, Cloud Computing, DevOps, Infrastructure as Code, Kubernetes, Automation, Observability, DevSecOps and MLOps.

The objective is not just to learn tools. It is to understand how modern applications are built, deployed, secured, monitored, maintained and operated in production-like environments.

---

## 1. Project Overview

This repository documents a structured 24-week learning and engineering journey from foundational knowledge to production-oriented Cloud, DevOps and MLOps practices.

It focuses on practical implementation, real-world engineering scenarios, troubleshooting, automation and technical documentation.

### Primary Goal

Develop the technical knowledge and practical confidence required to work as a:

**Cloud + DevOps Engineer → DevOps Engineer → Cloud/MLOps Engineer**

### What We Are Building

A complete local DevOps engineering laboratory capable of simulating modern software delivery and infrastructure workflows without provisioning paid cloud infrastructure.

The laboratory will support:

- Linux system administration.
- Application containerization.
- Automated CI/CD pipelines.
- Infrastructure as Code.
- Kubernetes orchestration.
- Configuration management.
- Cloud architecture simulations.
- Monitoring and centralized logging.
- Security scanning and DevSecOps.
- Machine learning deployment workflows.

---

## 2. Learning Philosophy

This roadmap follows an engineering-first learning approach.

The focus is on understanding why a technology exists, how it works internally, how it is configured and how it behaves when something fails.

### Our Learning Methodology

| Learning Area | Focus |
|---|---|
| Fundamentals | Understand architecture and concepts. |
| Hands-on | Implement everything locally. |
| Real-world Scenarios | Simulate practical engineering tasks. |
| Troubleshooting | Investigate and resolve failures. |
| Automation | Reduce repetitive manual operations. |
| Documentation | Maintain professional technical documentation. |
| Assessment | Validate knowledge independently. |

### 70% Practical + 20% Concepts + 10% Documentation

The emphasis is on building, breaking, debugging and rebuilding systems.

Watching tutorials alone does not count as completing a module.

---

## 3. Technology Roadmap

### Phase 1 – Linux, Networking and Git
**Weeks 1–3**

Technologies:
- Ubuntu Linux
- Bash
- Linux system administration
- TCP/IP
- DNS
- SSH
- Git

Learning objectives:
- Understand Linux architecture and filesystem hierarchy.
- Manage users, groups and permissions.
- Monitor processes, memory and storage.
- Manage services and investigate system logs.
- Understand networking and connectivity.
- Work with Git branches, merges and version control.

Practical outcome:
A Linux administration and troubleshooting laboratory.

Status: In Progress

### Phase 2 – Docker and Containerization
**Weeks 4–5**

Technologies:
- Docker
- Docker Compose
- Dockerfiles
- Container networking
- Container volumes

Learning objectives:
- Understand Docker architecture.
- Build and optimize Docker images.
- Containerize applications.
- Configure persistent storage.
- Connect multiple containers.
- Troubleshoot container failures.
- Implement container security practices.

Practical outcome:
A multi-tier containerized application.

Status: Planned

### Phase 3 – CI/CD Engineering
**Weeks 6–8**

Technologies:
- Jenkins
- GitLab CI/CD
- GitHub Actions
- Maven
- SonarQube
- JFrog Artifactory
- JUnit
- JaCoCo

Learning objectives:
- Design automated CI/CD pipelines.
- Configure Jenkins controllers and agents.
- Build reusable pipeline templates.
- Integrate automated testing.
- Implement code-quality gates.
- Publish and promote artifacts.
- Automate application deployments.

Practical outcome:
An end-to-end automated CI/CD pipeline.

Status: Planned

### Phase 4 – AWS Cloud Engineering
**Weeks 9–11**

Technologies:
- AWS IAM
- EC2
- VPC
- S3
- EBS
- RDS
- DynamoDB
- Route 53
- CloudWatch
- CloudTrail
- AWS CLI

Learning objectives:
- Understand AWS architecture and global infrastructure.
- Design secure VPC architectures.
- Understand IAM and least-privilege access.
- Understand compute, storage and networking services.
- Design highly available applications.
- Understand cloud monitoring and security.

Practical outcome:
Production-style AWS architecture designs and local service simulations.

Status: Planned

### Phase 5 – Infrastructure as Code
**Weeks 12–14**

Technologies:
- Terraform
- OpenTofu
- Terraform providers
- Modules
- State management
- Remote backend concepts

Learning objectives:
- Provision infrastructure declaratively.
- Develop reusable modules.
- Manage state files.
- Implement environment separation.
- Detect infrastructure drift.
- Integrate infrastructure validation into CI/CD.

Practical outcome:
A reusable Infrastructure as Code repository.

Status: Planned

### Phase 6 – Kubernetes and Helm
**Weeks 15–18**

Technologies:
- Kubernetes
- kind
- kubectl
- Helm
- Pods
- Deployments
- Services
- ConfigMaps
- Secrets
- StatefulSets
- Ingress

Learning objectives:
- Understand Kubernetes architecture.
- Deploy containerized applications.
- Configure application networking.
- Manage persistent storage.
- Implement scaling and health checks.
- Manage application releases using Helm.
- Troubleshoot production-style Kubernetes failures.

Practical outcome:
A multi-tier Kubernetes application deployment.

Status: Planned

### Phase 7 – Ansible, Observability and DevSecOps
**Weeks 19–21**

Technologies:
- Ansible
- Prometheus
- Grafana
- Alertmanager
- Loki
- Node Exporter
- Trivy
- Security scanning tools

Learning objectives:
- Automate Linux configuration.
- Develop reusable Ansible roles.
- Collect infrastructure and application metrics.
- Create monitoring dashboards.
- Configure alerts.
- Centralize application logs.
- Scan container images.
- Implement secure deployment practices.

Practical outcome:
An automated and monitored local infrastructure environment.

Status: Planned

### Phase 8 – Production Simulation and Interview Preparation
**Weeks 22–24**

Focus areas:
- End-to-end CI/CD implementation.
- Infrastructure automation.
- Kubernetes application deployments.
- Monitoring and alerting.
- Security integration.
- Incident investigation.
- Failure recovery.
- Deployment rollback.
- Technical interviews.

Practical outcome:
A documented, production-style DevOps platform.

Status: Planned

### Future Specialization – MLOps

After establishing the Cloud and DevOps foundation, extend the laboratory into MLOps.

Technologies to learn:
- Python
- MLflow
- Model packaging
- Model versioning
- Experiment tracking
- Docker-based model serving
- FastAPI
- Kubernetes-based inference
- Model monitoring
- CI/CD for machine learning

The goal is to understand how machine learning models move from experimentation to reliable deployment and monitoring.

---

## 4. Local Laboratory Architecture

The entire training environment is designed to run locally.

### Environment

| Component | Technology |
|---|---|
| Host Operating System | Windows 11 |
| Linux Environment | WSL2 + Ubuntu |
| Code Editor | Visual Studio Code |
| Version Control | Git |
| Container Runtime | Docker Desktop |
| Local Kubernetes | kind |
| CI/CD | Jenkins |
| Code Quality | SonarQube |
| Artifact Management | JFrog Artifactory |
| Infrastructure as Code | Terraform / OpenTofu |
| Configuration Management | Ansible |
| Monitoring | Prometheus |
| Dashboards | Grafana |
| Logging | Loki |
| Security Scanning | Trivy |
| MLOps | MLflow |

### Infrastructure Cost Policy

**Strict $0 Cloud Infrastructure Budget**

This project will not depend on paid cloud infrastructure.

Principles:

- No paid EC2 instances.
- No paid NAT gateways.
- No paid load balancers.
- No paid managed Kubernetes clusters.
- No paid cloud databases.
- No paid cloud monitoring services.
- No paid cloud trials or subscriptions.

All practical exercises will use local infrastructure, open-source software, simulated APIs and architecture exercises.

Note: Software licensing, local hardware, electricity and internet access are separate from cloud infrastructure costs. Free-tier limits and software licensing conditions must be respected.

---

## 5. Real-World Engineering Scenarios

This repository prioritizes scenarios commonly encountered in Cloud and DevOps engineering.

### Linux
- Disk usage reaches 95%.
- Application service fails to start.
- Process consumes excessive CPU.
- Permission denied errors.
- Network connectivity issues.

### Docker
- Container repeatedly restarts.
- Image size is unnecessarily large.
- Application cannot connect to the database.
- Container cannot access persistent storage.
- Container runs out of memory.

### CI/CD
- Pipeline fails during build.
- Unit tests fail.
- SonarQube quality gate blocks deployment.
- Artifact publishing fails.
- Deployment introduces a regression.

### AWS
- IAM permission denied.
- Application cannot reach an S3 bucket.
- VPC routing is incorrect.
- Security group blocks traffic.
- Architecture needs high availability.

### Terraform
- Infrastructure drift.
- State inconsistency.
- Incorrect resource configuration.
- Module dependency issues.
- Failed plan or apply.

### Kubernetes
- CrashLoopBackOff.
- ImagePullBackOff.
- Pod stuck in Pending.
- Service returns HTTP 503.
- Deployment rollback required.

### Monitoring
- Prometheus target is down.
- Grafana dashboard shows missing metrics.
- Application latency increases.
- Alert is not triggered.
- Disk or memory utilization becomes critical.

### DevSecOps
- Vulnerable container image.
- Hardcoded credentials.
- Excessive permissions.
- Failed dependency scan.
- Insecure deployment configuration.

---

## 6. Repository Structure

```text
cloud-devops-zero-to-production/
│
├── README.md
│
├── 01-linux/
│   ├── README.md
│   ├── day-01-environment/
│   ├── day-02-filesystem/
│   ├── day-03-users-permissions/
│   ├── day-04-process-services/
│   ├── day-05-monitoring/
│   ├── day-06-networking-ssh/
│   └── day-07-production-simulation/
│
├── 02-networking/
│
├── 03-docker/
│
├── 04-cicd/
│   ├── jenkins/
│   ├── gitlab/
│   ├── github-actions/
│   └── integrations/
│
├── 05-aws/
│
├── 06-terraform/
│
├── 07-kubernetes/
│
├── 08-ansible/
│
├── 09-monitoring/
│
├── 10-devsecops/
│
├── 11-mlops/
│
├── capstone-projects/
│
└── documentation/
    ├── architecture/
    ├── troubleshooting/
    ├── interview-preparation/
    └── learning-notes/
```

---

## 7. Learning and Assessment Standards

Each module must include:

1. Technology fundamentals.
2. Architecture understanding.
3. Installation and configuration.
4. Command reference.
5. Hands-on exercises.
6. Real-world scenarios.
7. Troubleshooting exercises.
8. Independent practical assessment.
9. Technical documentation.

### Weekly Assessment

Each module is evaluated on:

- Conceptual understanding.
- Practical implementation.
- Troubleshooting capability.
- Technical explanation.
- Documentation quality.

Minimum passing score: 75/100.

A module is considered complete only after its practical assessment.

---

## 8. Progress Tracker

| Phase | Duration | Status |
|---|---|---|
| Linux Administration | Weeks 1–3 | In Progress |
| Docker | Weeks 4–5 | Planned |
| CI/CD Engineering | Weeks 6–8 | Planned |
| AWS Cloud | Weeks 9–11 | Planned |
| Terraform | Weeks 12–14 | Planned |
| Kubernetes | Weeks 15–18 | Planned |
| Ansible + Observability + Security | Weeks 19–21 | Planned |
| Production Simulation | Weeks 22–24 | Planned |
| MLOps Specialization | Future extension | Planned |

---

## 9. How to Use This Repository

This repository is intended to be a practical engineering learning environment.

For every module:

1. Read the concepts and architecture.
2. Set up the required local environment.
3. Execute the hands-on exercises.
4. Implement the assigned scenario.
5. Intentionally introduce failures where safe.
6. Troubleshoot and document the solution.
7. Complete the assessment.
8. Commit the completed work to GitHub.

Suggested commit convention:

```text
docs: update learning documentation
feat: implement practical exercise
test: add assessment scenarios
fix: resolve configuration issue
chore: update lab environment
```

---

## 10. Final Objective

At the end of this roadmap, the goal is to independently:

- Administer Linux systems.
- Troubleshoot networking and application issues.
- Build and optimize Docker images.
- Develop automated CI/CD pipelines.
- Understand and design AWS architectures.
- Automate infrastructure using Terraform.
- Deploy and troubleshoot Kubernetes workloads.
- Automate configuration using Ansible.
- Implement monitoring and centralized logging.
- Integrate security into software delivery.
- Build and operate ML deployment workflows.

The final measure of success is not the number of technologies listed on a resume.

It is the ability to design, implement, explain, troubleshoot and maintain reliable engineering systems.

---

## Project Principles

**Learn deeply. Build practically. Break safely. Debug systematically. Document professionally.**

**Cloud Infrastructure Budget: $0**

**Roadmap: 24 Weeks + MLOps Specialization**

**Career Direction: Cloud + DevOps + MLOps Engineering**
