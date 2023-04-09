# BUSLOG = SERVICE1
SERVICE1_COMMIT_MSGS = [
    "Fix issue with buslog service failing to start on Kubernetes cluster",
    "Add error handling for buslog service API requests",
    "Update buslog service documentation with latest usage instructions",
    "Refactor buslog service code for improved performance",
    "Fix bug in buslog service causing data inconsistency in database",
    "Add support for custom logging configurations in buslog service",
    "Implement API versioning in buslog service for backward compatibility",
    "Update dependencies in buslog service to latest versions",
    "Improve logging output in buslog service for better debugging",
    "Fix security vulnerability in buslog service's authentication logic",
    "Add unit tests for buslog service to improve test coverage",
    "Refactor buslog service's database queries for better efficiency",
    "Improve error handling for database connections in buslog service",
    "Add support for Kubernetes Pod scaling in buslog service deployment",
    "Fix issue with buslog service's message processing logic",
    "Update buslog service's Dockerfile for better containerization",
    "Add support for custom log formats in buslog service",
    "Refactor buslog service's configuration management for better scalability",
    "Fix bug in buslog service's message validation logic",
]

# CTRLR = SERVICE2
SERVICE2_COMMIT_MSGS = [
    "Fix issue with ctrlr service failing to authenticate with external API",
    "Add error handling for ctrlr service API requests",
    "Update ctrlr service documentation with latest usage instructions",
    "Refactor ctrlr service code for improved performance",
    "Fix bug in ctrlr service causing incorrect data processing",
    "Add support for custom configurations in ctrlr service",
    "Implement API versioning in ctrlr service for backward compatibility",
    "Update dependencies in ctrlr service to latest versions",
    "Improve logging output in ctrlr service for better debugging",
    "Fix security vulnerability in ctrlr service's authentication logic",
    "Add unit tests for ctrlr service to improve test coverage",
    "Refactor ctrlr service's database queries for better efficiency",
    "Improve error handling for external API connections in ctrlr service",
    "Add support for Kubernetes Pod scaling in ctrlr service deployment",
    "Fix issue with ctrlr service's processing logic",
    "Update ctrlr service's Dockerfile for better containerization",
    "Add support for custom log formats in ctrlr service",
    "Refactor ctrlr service's configuration management for better scalability",
    "Fix bug in ctrlr service's validation logic",
]

# FLASKUI = SERVICE3
SERVICE3_COMMIT_MSGS = [
    "Fix issue with flask-ui service failing to render template in Kubernetes cluster",
    "Add error handling for flask-ui service API requests",
    "Update flask-ui service documentation with latest usage instructions",
    "Refactor flask-ui service code for improved performance",
    "Fix bug in flask-ui service causing incorrect data rendering",
    "Add support for custom configurations in flask-ui service",
    "Implement API versioning in flask-ui service for backward compatibility",
    "Update dependencies in flask-ui service to latest versions",
    "Improve logging output in flask-ui service for better debugging",
    "Fix security vulnerability in flask-ui service's authentication logic",
    "Add unit tests for flask-ui service to improve test coverage",
    "Refactor flask-ui service's database queries for better efficiency",
    "Improve error handling for database connections in flask-ui service",
    "Add support for Kubernetes Pod scaling in flask-ui service deployment",
    "Fix issue with flask-ui service's template rendering logic",
    "Update flask-ui service's Dockerfile for better containerization",
    "Add support for custom log formats in flask-ui service",
    "Refactor flask-ui service's configuration management for better scalability",
    "Fix bug in flask-ui service's form validation logic'"
]

SERVICE_COMMIT_MSGS = [
    "Fix bug in function xyz",
    "Refactor code for improved readability",
    "Add feature ABC",
    "Update documentation",
    "Optimize performance",
    "Merge branch feature/123",
    "Fix typo in file XYZ",
    "Implement new functionality",
    "Update dependencies",
    "Add test cases",
    "Fix formatting issues",
    "Remove unused code",
    "Fix security vulnerability",
    "Update error handling",
    "Revert previous commit",
    "Add logging statements",
    "Refactor variable naming",
    "Update UI layout",
    "Fix edge case in function ABC",
    "Improve error messages"
]

CODE_LINES_LIST = ['from kubernetes import client, config',
                   'config.load_kube_config()',
                   'v1 = client.CoreV1Api()',
                   'ret = v1.list_pod_for_all_namespaces(watch=False)',
                   'print("Total pods: %d" % len(ret.items))',
                   'ret = v1.list_node(watch=False)',
                   'print("Total nodes: %d" % len(ret.items))',
                   'v1_beta = client.ExtensionsV1beta1Api()',
                   'ret = v1_beta.list_deployment_for_all_namespaces(watch=False)',
                   'print("Total deployments: %d" % len(ret.items))',
                   'ret = v1_beta.list_ingress_for_all_namespaces(watch=False)',
                   'print("Total ingresses: %d" % len(ret.items))',
                   'ret = v1_beta.list_replica_set_for_all_namespaces(watch=False)',
                   'print("Total replica sets: %d" % len(ret.items))',
                   'v1_apps = client.AppsV1Api()',
                   'ret = v1_apps.list_stateful_set_for_all_namespaces(watch=False)',
                   'print("Total stateful sets: %d" % len(ret.items))',
                   'ret = v1_apps.list_daemon_set_for_all_namespaces(watch=False)',
                   'print("Total daemon sets: %d" % len(ret.items))']

PULL_REQUESTS_TOPICS = [
    "Fix issue with authentication flow",
    "Add support for multi-factor authentication",
    "Update documentation with new usage instructions",
    "Refactor code to improve performance",
    "Implement feature to support file uploads",
    "Fix bug causing incorrect calculation of prices",
    "Add unit tests for critical functionality",
    "Implement error handling for edge cases",
    "Add support for internationalization and localization",
    "Improve logging and error reporting",
    "Refactor database schema to optimize queries",
    "Implement caching to improve response times",
    "Fix UI rendering issue on mobile devices",
    "Add support for OAuth authentication",
    "Implement pagination for large datasets",
    "Add support for custom themes",
    "Improve error messaging for user-friendly feedback",
    "Refactor code to follow coding style guidelines",
    "Fix cross-site scripting (XSS) vulnerability",
    "Implement user authentication via social media accounts",
]
BRANCHES_NAMES_PREFIXES = [
    "feature/",
    "bugfix/",
    "hotfix/",
    "develop/",
    "refactor/",
    "chore/",
    "test/",
    "style/",
    "improvement/",
    "task/",
    "experimental/",
    "revert/",
    "support/",
    "temp/",
    "review/",
    "fix/",
    "vendor/",
    "maintenance/",
    "release-notes/",
    "demo/",
    "design/",
    "analysis/",
    "backlog/"
]

BRANCHES_NAMES = [
    "Containerization-best-practices",
    "Microservices-architecture-refinement",
    "Kubernetes-deployment-optimization",
    "Infrastructure-as-code-refactoring",
    "Continuous-integration-streamlining",
    "DevOps-automation-enhancement",
    "Scalability-improvement-refactoring",
    "Distributed-tracing-implementation",
    "Service-mesh-adoption-refactoring",
    "Cloud-native-migration-refactoring",
    "Immutable-infrastructure-implementation",
    "Configuration-management-refinement",
    "Monitoring-and-observability-improvement",
    "Blue-green-deployment-optimization",
    "GitOps-principles-adoption",
    "CI/CD-pipeline-optimization",
    "Deployment-strategy-refactoring",
    "Performance-tuning-refactoring",
    "Error-handling-enhancement-refactoring",
    "Security-hardening-refactoring",
    "Logging-and-auditing-improvement",
    "Secrets-management-refactoring",
    "Auto-scaling-improvement-refactoring",
    "Infrastructure-cost-optimization",
    "Backup-and-recovery-strategy-refactoring",
    "Compliance-and-audit-enhancement",
    "Release-management-optimization",
    "Load-balancing-configuration-refinement",
    "Pod-scheduling-error",
    "Service-discovery-issue",
    "Ingress-configuration-bug",
    "Persistent-volume-claim-error",
    "Container-image-vulnerability",
    "Configmap-or-Secrets-misconfiguration",
    "Kubernetes-API-error",
    "Networking-issue-in-Kubernetes-cluster",
    "Resource-quota-violation-error",
    "RBAC-permission-error",
    "Pod-crash-loop-backoff-issue",
    "Node-drain-or-failure-error",
    "Kubernetes-upgrade-issue",
    "Pod-lifecycle-bug",
    "CronJob-scheduling-error",
    "DNS-resolution-issue",
    "Service-mesh-configuration-bug",
    "Kubernetes-operators-error",
    "Custom-resource-definition-issue",
    "Kubernetes-statefulset-bug",
    "Kubernetes-volume-bug",
    "Kubernetes-pod-networking-bug",
    "Ingress-controller-bug",
    "Kubernetes-namespace-error",
    "Kubernetes-security-context-bug",
    "Kubernetes-apiServer-configuration-issue",
    "Pod-scaling-error",
    "Kubernetes-autoscaling-issue",
    "Kubernetes-admission-controller-error",
]

JIRA_TICKETS = [
    {
        "summary": "BUG: Pod CrashLoopBackOff error after deploying k8s application",
        "description": "The k8s application's pods are crashing with a 'CrashLoopBackOff' error in the logs, indicating a recurring issue. Investigation needed to identify and resolve the root cause of the problem.",
        "issuetype": "Bug"
    },
    {
        "summary": "Enhancement Request: Add support for rolling updates in k8s application",
        "description": "Currently, the k8s application does not support rolling updates, resulting in downtime during deployments. Requesting to add support for rolling updates to ensure zero-downtime deployments and better availability.",
        "issuetype": "Idea"
    },
    {
        "summary": "BUG: Ingress not routing traffic to k8s application",
        "description": "Ingress configuration is not routing incoming traffic to the k8s application's services, resulting in 404 errors. Investigation needed to identify the misconfiguration and fix it to enable proper traffic routing.",
        "issuetype": "Bug"
    },
    {
        "summary": "Enhancement Request: Implement horizontal pod autoscaling for k8s application",
        "description": "Requesting to implement horizontal pod autoscaling for the k8s application to automatically scale up or down based on resource utilization and traffic patterns, ensuring optimal performance and resource utilization.",
        "issuetype": "Idea"
    },
    {
        "summary": "BUG: Container image pull failure in k8s application",
        "description": "The k8s application's pods are failing to pull container images from the container registry, resulting in failed deployments. Investigation needed to resolve the issue and ensure successful image pulling during deployments.",
        "issuetype": "Bug"
    },
    {
        "summary": "Enhancement Request: Add logging and monitoring to k8s application",
        "description": "Requesting to add proper logging and monitoring to the k8s application to enable better observability and troubleshooting. This includes setting up centralized logging and monitoring solutions like ELK stack or Prometheus/Grafana.",
        "issuetype": "Idea"
    },
    {
        "summary": "BUG: CrashLoopBackOff in init container of k8s application",
        "description": "The init containers in the k8s application's pods are encountering 'CrashLoopBackOff' error, preventing the pods from starting properly. Investigation needed to identify and fix the issue in the init container configuration.",
        "issuetype": "Bug"
    },
    {
        "summary": "Enhancement Request: Implement rolling restarts for k8s application",
        "description": "Requesting to implement rolling restarts for the k8s application to gracefully restart pods one by one, avoiding downtime and ensuring uninterrupted service availability during restarts.",
        "issuetype": "Idea"
    },
    {
        "summary": "BUG: Incorrect resource limits set in k8s application",
        "description": "The resource limits set for the k8s application's pods are incorrect, resulting in resource exhaustion and performance issues. Investigation needed to review and adjust the resource limits for optimal performance and stability.",
        "issuetype": "Bug"
    },
    {
        "summary": "Enhancement Request: Add support for canary deployments in k8s application",
        "description": "Requesting to add support for canary deployments in the k8s application to enable gradual rollouts and rollbacks, minimizing the impact of faulty deployments and ensuring better resilience and fault tolerance.",
        "issuetype": "Idea"
    },
    {
        "summary": "BUG: Flask-UI service returning 500 error on login",
        "description": "The Flask-UI service is returning a 500 error when users attempt to log in, resulting in login failures. Investigation needed to identify and fix the issue to ensure successful user authentication and login functionality.",
        "issuetype": "Bug"
    },
    {
        "summary": "Enhancement Request: Add support for multi-factor authentication in Flask-UI service",
        "description": "Requesting to add support for multi-factor authentication (MFA) in the Flask-UI service to provide an additional layer of security for user authentication. This will help in mitigating the risk of unauthorized access to the service and user accounts.",
        "issuetype": "Idea"
    },
    {
        "summary": "BUG: Flask-UI service not rendering UI components properly",
        "description": "The Flask-UI service is not rendering UI components properly, resulting in broken or misaligned user interface elements. Investigation needed to identify and fix the issue to ensure proper rendering of UI components for improved user experience.",
        "issuetype": "Bug"
    },
    {
        "summary": "Enhancement Request: Implement API rate limiting in Flask-UI service",
        "description": "Requesting to implement API rate limiting in the Flask-UI service to prevent abuse and protect against potential DDoS attacks. This will help in ensuring fair usage of the service and maintaining service availability and performance.",
        "issuetype": "Idea"
    },
    {
        "summary": "BUG: Flask-UI service experiencing high memory utilization",
        "description": "The Flask-UI service is experiencing high memory utilization, resulting in performance degradation and increased response times. Investigation needed to identify the memory-intensive processes and optimize resource utilization for improved performance and responsiveness.",
        "issuetype": "Bug"
    },
    {
        "summary": "Enhancement Request: Add support for internationalization (i18n) in Flask-UI service",
        "description": "Requesting to add support for internationalization (i18n) in the Flask-UI service to enable localization of user interface components for different languages and regions. This will help in providing a better user experience for users from diverse language backgrounds.",
        "issuetype": "Idea"
    },
    {
        "summary": "BUG: Flask-UI service failing to handle concurrent user requests",
        "description": "The Flask-UI service is failing to handle concurrent user requests, resulting in degraded performance and increased response times. Investigation needed to identify and fix the issue with request handling to ensure efficient handling of concurrent user requests.",
        "issuetype": "Bug"
    },
    {
        "summary": "Enhancement Request: Implement container image scanning in Flask-UI service",
        "description": "Requesting to implement container image scanning in the Flask-UI service to ensure the security and integrity of container images used in the service. This will help in identifying and addressing potential security vulnerabilities and ensuring secure container deployments.",
        "issuetype": "Idea"
    },
    {
        "summary": "BUG: Flask-UI service not persisting user preferences properly",
        "description": "The Flask-UI service is not persisting user preferences properly, resulting in loss of user settings and configurations. Investigation needed to identify and fix the issue with user preference storage to ensure reliable persistence of user preferences across sessions.",
        "issuetype": "Bug"
    },
    {
        "summary": "Enhancement Request: Add support for role-based access control (RBAC) in Flask-UI service",
        "description": "Requesting to add support for role-based access control (RBAC) in the Flask-UI service to provide granular control over user permissions and access to different functionalities and resources.",
        "issuetype": "Idea"
    }
]

PYTHON_COMMANDS = [
    "print('Hello, world!')",
    "input('Enter your name: ')",
    "len('Hello')",
    "range(1, 10)",
    "list('Python')",
    "tuple((1, 2, 3))",
    "set([1, 2, 3, 4])",
    "dict({'a': 1, 'b': 2})",
    "sorted([4, 2, 1, 3])",
    "str.upper('hello')",
    "int('42')",
    "float(3.14)",
    "bool(0)",
    "abs(-5)",
    "sum([1, 2, 3, 4])",
    "max([1, 2, 3, 4])",
    "min([1, 2, 3, 4])",
    "pow(2, 3)",
    "round(3.14159, 2)",
    "hex(255)",
    "bin(255)",
    "oct(255)",
    "ord('A')",
    "chr(65)",
    "type('hello')",
    "isinstance(42, int)",
    "dir('hello')",
    "help(print)"
]

PULL_REQUESTS_TITLES = [
    "Add Prometheus monitoring support for Trio microservices",
    "Refactor Trio buslog microservice for better performance",
    "Implement authentication and authorization in Trio ctrlr microservice",
    "Update Flask-UI frontend for Trio with new UI design",
    "Integrate logging framework into Trio buslog microservice",
    "Improve error handling in Trio ctrlr microservice",
    "Add unit tests for Trio Flask-UI frontend",
    "Optimize Trio buslog microservice for scalability",
    "Implement CI/CD pipeline for Trio microservices",
    "Update dependencies for Trio buslog, ctrlr, and Flask-UI",
    "Implement caching mechanism in Trio ctrlr microservice",
    "Refactor Trio Flask-UI for improved code maintainability",
    "Add API documentation for Trio buslog, ctrlr, and Flask-UI",
    "Implement graceful shutdown handling in Trio microservices",
    "Update logging configuration in Trio buslog microservice",
    "Enhance error handling in Trio Flask-UI frontend",
    "Implement circuit breaker pattern in Trio ctrlr microservice",
    "Add support for Kubernetes namespaces in Trio microservices",
    "Refactor Trio buslog microservice to use async I/O",
    "Update UI components in Trio Flask-UI for better usability",
    "Implement load balancing in Trio ctrlr microservice",
    "Add Prometheus metrics endpoint to Trio microservices",
    "Implement API versioning in Trio buslog, ctrlr, and Flask-UI",
    "Enhance security measures in Trio microservices",
    "Update logging format in Trio buslog microservice",
    "Implement rate limiting in Trio ctrlr microservice",
    "Refactor Trio Flask-UI for improved performance",
    "Add custom exception handling in Trio microservices",
    "Update documentation for Trio buslog, ctrlr, and Flask-UI",
    "Implement distributed tracing in Trio microservices"
]
