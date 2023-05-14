# Headline

Selectively enable TCP/IP SERVICEs/OPEN PORTS

# Key Benefits

Any active [listener](#DEF_Listener) is a potential avenue for attack; not only do [listeners](#DEF_Listener) have bugs, but dispatching traffic to a [listener](#DEF_Listener) usually uses more system resources than discarding that traffic in a lower layer, creating a denial of service vulnerability.

Nearly all security experts recommend disabling unneeded services whenever possible, and many customers have operating procedures based on those recommendations.

[TCP/IP services](#DEF_TcpIpService) are the most visible class of [listeners](#DEF_Listener), one of the most frequently attacked classes, and the class most often subject to customer scrutiny. We have therefore chosen to address [TCP/IP services](#DEF_TcpIpService) in this requirement.

Fine-grained control is essential, since coarser control usually forces users to enable many unneeded services.

Filters, even within a single operating system kernel, are prone to failure; it's usually easy for a developer or system administrator to make an error in creating a filter, or to make a change that creates a path around an existing filter without realizing it.

# Description

Customers shouldn't have to let unneeded services run on their devices.

# Behavior

## SEC-OFF-PROC-FR1: Enabling or Disabling TCP/IP Services

1. It _MUST_ be possible for an [administrator](#DEF_Administrator) to separately enable or disable each provided [TCP/IP service](#DEF_TcpIpService) which is not [essential](#DEF_Essential) to the [product](#DEF_Product), except that any set of [TCP/IP services](#DEF_TcpIpService) which are [mutually essential](#DEF_MutuallyEssential) may be configured as a group.

2. It is not enough to apply a filter at some lower layer to keep traffic from reaching the [listener](#DEF_Listener) associated with the [TCP/IP service](#DEF_TcpIpService). The [listener](#DEF_Listener) itself _MUST_ be disabled, e.g. by not starting a process, not starting a thread, or not issuing a listen() call.

## SEC-OFF-PROC-FR2: Additional Rules for Container Environments

1. Container environments employ multiple [listener](#DEF_Listener) that are enabled by default for ease of use. These [listeners](#DEF_Listener) _MUST_ be disabled or filtered such that they are accessible only from localhost or they _MUST_ be authenticated.

2. Specifically, the following [listeners](#DEF_Listener) _MUST_ be considered:

    1. Kubernetes cluster API: The Kubernetes cluster API is used to read and write Kubernetes resource objects such as workloads, discovery and load balancing, config and storage, cluster resources, and metadata. Failing to secure this [listener](#DEF_Listener) gives anyone with API access administrative control over the Kubernetes cluster and application.

    2. Docker Engine API: The Docker Engine API is used to control both Docker and Docker Swarm. It is a [listener](#DEF_Listener) that gives anyone with API access administrative control over the Docker environment. This includes access to container CRUD, inspection, processes, file system, resources, etc.

## SEC-OFF-PROC-FR3: Funtions other than TCP/IP Services

1. Similar Configurability _SHOULD_ be similar for functions other than [TCP/IP services](#DEF_TcpIpService), and especially for [listeners](#DEF_Listener). Such configurability is likely to be a _MUST_ for various classes of [listeners](#DEF_Listener) in the future.

# History

```yaml
-----
affected_psb: SEC-OFF-PROC
description:  Updated to functional requirements. 

```

# Attributes

    phase: requirements
    legallysensitive: false
    priority: 8
    applicability:
    - force: mandatory
      target:
        restrict: |-
          products
    category: Threat Surface Reduction
    riskArea: System Hardening
    waivable: true
    version: 1
    id: SEC-OFF-PROC
    issueref: ISS_SurpriseListener
    tags:
    - EN/PI
    - PSB/OnPrem
    - EN/PI DT
