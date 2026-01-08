<h1>🚀 Containerized Microservice Application on AWS (EKS)</h1>
As cloud-native technologies continue to evolve, microservices have become the preferred architectural approach for building modern, resilient, and scalable applications. By designing applications as a collection of loosely coupled services, development teams can achieve faster deployments, improved fault isolation, and greater operational flexibility.
<img width="1125" height="478" alt="image" src="https://github.com/user-attachments/assets/31630c3d-7aed-42c6-8398-44964e5bba91" />


<h2>📌 Project Overview</h2>
<p>
  This project demonstrates the design, containerization, CI/CD automation, and deployment of a
  <strong>Flask-based microservice application</strong> on <strong>Amazon EKS</strong>.
  It follows cloud-native best practices using <strong>Docker</strong>, <strong>AWS CodeBuild</strong>,
  <strong>CodePipeline</strong>, <strong>ECR</strong>, <strong>S3</strong>, <strong>IAM</strong>, and
  <strong>Kubernetes</strong> to deliver a fully automated deployment workflow.
</p>

<h2>🏗 Architecture Overview</h2>
<ul>
  <li><strong>Frontend Service</strong> exposed externally using an AWS LoadBalancer</li>
  <li><strong>Backend Microservices</strong> including User, Product, and Order services</li>
  <li><strong>Container Registry</strong> using Amazon ECR</li>
  <li><strong>CI/CD Pipeline</strong> triggered by GitHub commits</li>
  <li><strong>Orchestration Platform</strong> using Amazon EKS</li>
</ul>

<h2>🧩 Implementation Steps</h2>

<h3>1) Microservice Application Development</h3>
<ul>
  <li>Developed independent Flask-based microservices.</li>
  <li>Ensured loose coupling and scalability between services.</li>
  <li>Structured the application to support containerized and Kubernetes-based deployment.</li>
</ul>

<h3>2) Containerization &amp; Local Validation</h3>
<ul>
  <li>Containerized each microservice using individual Dockerfiles.</li>
  <li>Orchestrated services locally using Docker Compose.</li>
  <li>Validated application behavior on an EC2 Linux instance before cloud deployment.</li>
</ul>

<h3>3) Continuous Integration with AWS CodeBuild</h3>
<ul>
  <li>Integrated GitHub repository with AWS CodeBuild using webhooks.</li>
  <li>Created dedicated Amazon ECR repositories for each microservice.</li>
  <li>Configured CodeBuild to build and push Docker images to ECR and generate deployment artifacts.</li>
  <li>Stored build artifacts in an Amazon S3 bucket.</li>
  <li>Enabled CloudWatch logging for monitoring and troubleshooting.</li>
  <li>Secured credentials using environment variables and AWS Secrets Manager.</li>
</ul>

<h3>4) Amazon EKS Cluster Setup</h3>
<ul>
  <li>Created an Amazon EKS cluster and managed worker node groups using AWS CLI.</li>
  <li>Configured IAM roles and permissions required for Kubernetes access.</li>
  <li>Updated the <code>aws-auth</code> ConfigMap to allow nodes to join the cluster and enable CodeBuild deployments.</li>
</ul>

<h3>5) Kubernetes Deployment Configuration</h3>
<ul>
  <li>Created Kubernetes manifests for all microservices.</li>
  <li>Exposed the frontend using a LoadBalancer for external access.</li>
  <li>Exposed backend services using ClusterIP for internal communication only.</li>
  <li>Applied Kubernetes security best practices by limiting service exposure.</li>
</ul>

<h3>6) CI/CD Deployment to EKS</h3>
<ul>
  <li>Extended the CI pipeline to deploy applications directly to EKS.</li>
  <li>On every GitHub commit: images are rebuilt, pushed to ECR, and manifests are applied to EKS automatically.</li>
  <li>Achieved a fully automated end-to-end CI/CD workflow from commit to live deployment.</li>
</ul>

<h3>7) Application Access</h3>
<ul>
  <li>Application is accessible via the AWS LoadBalancer DNS endpoint exposed by the frontend service.</li>
  <li>Verified end-to-end functionality and inter-service communication in the EKS cluster.</li>
</ul>

<h3>8) Monitoring &amp; Troubleshooting</h3>
<ul>
  <li>Used CloudWatch logs to monitor build and deployment stages.</li>
  <li>Validated IAM role mappings and EKS permissions.</li>
  <li>Ensured CodeBuild role access within the <code>aws-auth</code> ConfigMap.</li>
  <li>Followed best practice by using the CodeBuild Standard 7.0 image for built-in Docker, AWS CLI, and Kubernetes tools.</li>
</ul>

<h2>✅ Key Highlights</h2>
<ul>
  <li>End-to-end <strong>cloud-native microservice deployment</strong> on AWS</li>
  <li>Fully automated <strong>CI/CD pipeline</strong> (GitHub → CodeBuild/CodePipeline → EKS)</li>
  <li>Secure image storage using <strong>Amazon ECR</strong></li>
  <li>Scalable container orchestration with <strong>Amazon EKS</strong></li>
  <li>Strong focus on <strong>automation</strong>, <strong>security</strong>, and <strong>observability</strong></li>
</ul>
