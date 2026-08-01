# Day 2 - Mistakes Learned

---

# Objective

The purpose of this document is to record the mistakes and misconceptions I had while learning Spark Architecture. Reviewing these mistakes regularly helps reinforce the correct concepts and prevents repeating the same misunderstandings.

---

# Mistake 1: Thinking the Driver Processes the Data

## My Initial Thought

I initially thought that the Driver was responsible for processing the data because it controls the Spark application.

## Correct Understanding

The Driver does **not** process the data.

Its responsibilities are to:

- Coordinate the Spark application
- Create the execution plan
- Request resources
- Schedule tasks
- Monitor execution
- Collect results

The actual data processing is performed by the Executors.

## Lesson Learned

**Driver = Coordinator**

**Executor = Data Processor**

---

# Mistake 2: Thinking Worker Nodes Process the Data

## My Initial Thought

I assumed that Worker Nodes directly process the data.

## Correct Understanding

A Worker Node is simply a machine that provides CPU, memory and storage resources.

Executors run inside Worker Nodes and perform the actual computation.

## Lesson Learned

**Worker Node provides resources.**

**Executor performs the work.**

---

# Mistake 3: Assuming More Worker Nodes Always Improve Performance

## My Initial Thought

Whenever a Spark job becomes slow, I thought adding more Worker Nodes would solve the problem.

## Correct Understanding

A slow Spark job may be caused by:

- Data Skew
- Uneven Task Distribution
- Large Partitions
- CPU Bottlenecks
- Memory Bottlenecks
- Network Bottlenecks
- Storage Bottlenecks

Adding more machines without identifying the bottleneck may not improve performance.

## Lesson Learned

**Investigate first. Scale later.**

---

# Mistake 4: Confusing Driver Failure with Executor Failure

## My Initial Thought

I assumed Driver failure and Executor failure had the same impact.

## Correct Understanding

Executor failure is usually recoverable because Spark can recreate Executors and retry failed tasks.

Driver failure is more serious because the Driver coordinates the entire Spark application.

## Lesson Learned

**Executor Failure = Recoverable (in many cases)**

**Driver Failure = Much More Serious**

---

# Mistake 5: Believing Distributed Processing Automatically Means Balanced Processing

## My Initial Thought

I thought that if data was distributed across multiple machines, every machine would automatically receive an equal amount of work.

## Correct Understanding

Distributed processing does not guarantee balanced processing.

Some Executors may receive much larger partitions than others, resulting in uneven workload distribution.

## Lesson Learned

**Distributed ≠ Balanced**

---

# Mistake 6: Ignoring Data Skew

## My Initial Thought

I did not realize that uneven data distribution could become a major performance bottleneck.

## Correct Understanding

If one partition contains significantly more data than the others, the corresponding Executor will take much longer to finish.

This can delay the entire Spark job.

## Lesson Learned

Always investigate Data Skew when analyzing Spark performance.

---

# Mistake 7: Assuming a Busy Worker Node Means the Machine Is Slow

## My Initial Thought

If one Worker Node showed high CPU utilization, I assumed that machine itself was the problem.

## Correct Understanding

A busy Worker Node often indicates that it has been assigned more work than the others.

The issue may be related to task distribution or partition sizes rather than the machine itself.

## Lesson Learned

**Busy Worker ≠ Bad Worker**

Investigate the workload before blaming the infrastructure.

---

# Mistake 8: Thinking Spark Starts Processing Data Immediately

## My Initial Thought

I believed that creating a SparkSession immediately started processing data.

## Correct Understanding

Creating a SparkSession only starts the Spark application.

Actual data processing begins later when we work with DataFrames and execute Actions.

## Lesson Learned

**SparkSession starts the application, not the data processing.**

---

# Day 2 Key Takeaways

- The Driver coordinates the Spark application.
- Executors perform the actual data processing.
- Worker Nodes provide the required resources.
- The Cluster Manager allocates resources.
- Driver failure is more serious than Executor failure.
- Distributed processing does not always mean balanced processing.
- Data Skew can significantly slow down Spark jobs.
- Always identify the bottleneck before deciding to scale.
- Think like a Senior Data Engineer by investigating first and optimizing before adding resources.

---

# Final Reflection

The biggest lesson from Day 2 is that a good Data Engineer does not jump directly to a solution.

Instead, they:

1. Understand the problem.
2. Investigate the system.
3. Identify the bottleneck.
4. Optimize where possible.
5. Scale only when the evidence supports it.

> **Golden Rule:**  
> **Investigate → Identify Bottleneck → Optimize → Scale if Necessary**
