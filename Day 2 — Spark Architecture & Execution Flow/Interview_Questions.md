# Day 2 - Interview Questions

---

# Beginner Level

## Q1. Explain the complete Spark Architecture.

### Expected Answer

Spark Architecture consists of five major components:

- Spark Application
- Driver
- Cluster Manager
- Worker Nodes
- Executors

### Architecture Flow

    Spark Application
            ↓
         Driver
            ↓
    Cluster Manager
            ↓
      Worker Nodes
            ↓
        Executors
            ↓
           Tasks

The Driver coordinates the Spark Application.

The Cluster Manager allocates resources.

Worker Nodes provide the machine resources.

Executors process the assigned tasks.

---

## Q2. Why is the Driver called the Brain of the Spark Application?

### Expected Answer

The Driver is called the brain because it controls and coordinates the entire Spark Application.

Its responsibilities include:

- Creating the SparkSession
- Creating the execution plan
- Requesting resources from the Cluster Manager
- Scheduling tasks
- Sending tasks to Executors
- Monitoring execution
- Collecting results

The Driver coordinates the work.

Executors perform the work.

---

## Q3. Does the Driver process the data?

### Expected Answer

No.

The Driver mainly coordinates the Spark Application.

The actual data processing is performed by the Executors running on Worker Nodes.

If the Driver processed the entire dataset itself, there would be no advantage in using distributed computing.

---

## Q4. What is the responsibility of a Worker Node?

### Expected Answer

A Worker Node is a machine that provides CPU, Memory and Storage resources.

Executors run on Worker Nodes and use these resources to process Spark tasks.

Worker Node = Provides Resources

Executor = Performs Computation

---

## Q5. What is the responsibility of the Cluster Manager?

### Expected Answer

The Cluster Manager manages all the available resources in the cluster.

Its responsibilities include:

- Tracking available machines
- Allocating resources
- Starting Executors
- Managing resource requests from the Driver

---

# Intermediate Level

## Q6. Can one Worker Node have multiple Executors?

### Expected Answer

Yes.

A Worker Node can have multiple Executors depending on the available CPU cores and Memory.

If sufficient resources are available, multiple Executors can run on the same Worker Node.

---

## Q7. What happens if one Executor fails?

### Expected Answer

If an Executor fails, Spark can recreate the Executor and retry the failed tasks depending on the configuration.

The Driver continues coordinating the Spark Application.

Executor failure is generally recoverable.

---

## Q8. What happens if the Driver fails?

### Expected Answer

Driver failure is much more serious.

Since the Driver coordinates the Spark Application, Executors no longer know what work to perform.

The running Spark Application usually stops.

---

## Q9. Why is Driver failure more serious than Executor failure?

### Expected Answer

Because the Driver controls the entire Spark Application.

Executors only execute assigned tasks.

If an Executor fails, Spark may recover.

If the Driver fails, the application loses its coordinator and the job stops.

---

## Q10. What is the difference between a Worker Node and an Executor?

### Expected Answer

| Worker Node | Executor |
|-------------|----------|
| Physical/Virtual Machine | JVM Process |
| Provides CPU, Memory & Storage | Processes Spark Tasks |
| Hosts Executors | Executes Assigned Tasks |

---

# Senior Engineer Thinking

## Q11. A Spark job is slow. Your manager says, "Add more Worker Nodes." What will you do?

### Expected Answer

I would not immediately add more machines.

First I would investigate:

- Task Distribution
- Partition Distribution
- Data Skew
- Executor Utilization
- CPU Usage
- Memory Usage
- Network Bottlenecks
- Storage Bottlenecks

Only after identifying the actual bottleneck would I decide whether scaling is required.

---

## Q12. One Worker Node is using 90% CPU while the others are almost idle. What could be the reason?

### Expected Answer

Possible reasons include:

- Uneven Task Distribution
- Data Skew
- Large Partitions
- Uneven Executor Allocation

I would investigate why one Worker Node received significantly more work than the others before making any infrastructure changes.

---

## Q13. Why shouldn't we immediately add more machines?

### Expected Answer

Adding more machines increases infrastructure cost.

If the real problem is:

- Data Skew
- Uneven Task Distribution
- Large Partitions

Adding machines may not improve performance.

The bottleneck should always be identified first.

---

## Q14. How do you decide whether Spark is actually required?

### Expected Answer

I compare:

- Current Processing Time
- Business SLA
- Data Volume
- Future Data Growth
- Existing System Performance
- Infrastructure Cost
- Scalability Requirements

If the current solution already meets the business requirement, Spark may not be necessary.

---

## Q15. What is the biggest lesson from Day 2?

### Expected Answer

A Senior Data Engineer does not immediately think about technology.

Instead, they first understand:

- The Business Problem
- The Current Performance
- The Bottleneck
- The Available Resources
- The Scalability Requirement

Only then do they choose the appropriate solution.

---

# Day 2 - Quick Revision

## Remember These 15 Points

1. Understand the complete Spark Architecture.
2. Driver is the Brain of the Spark Application.
3. Driver coordinates; Executors process data.
4. Worker Nodes provide resources.
5. Cluster Manager allocates resources.
6. One Worker Node can have multiple Executors.
7. Executor failures are generally recoverable.
8. Driver failure is more serious than Executor failure.
9. Understand the difference between Worker Nodes and Executors.
10. Never add machines without investigation.
11. Check Task Distribution before scaling.
12. Data Skew can make one Worker Node overloaded.
13. Identify the bottleneck before choosing a solution.
14. Spark should be selected based on business requirements, not just data size.
15. Think like a Senior Data Engineer: **Investigate → Identify Bottleneck → Optimize → Scale if Necessary.**

---

# ⭐ Golden Interview Rule

> **Don't say:**

> "Let's use Spark."

Instead say:

> **"Let's understand the business problem, identify the bottleneck, and then decide whether Spark or scaling is actually required."**
