# 🚀 Day 1 - Interview Questions
# Big Data, Hadoop & Spark Fundamentals

---

# 🟢 Level 1 - Basic Questions

## Q1. Why was Distributed Computing introduced?

### Answer

Distributed Computing was introduced because a single machine cannot efficiently process very large amounts of data.

Instead of upgrading one expensive server, the work is divided among multiple machines that process data in parallel. This improves performance, scalability, and fault tolerance.

---

## Q2. What is Big Data?

### Answer

Big Data is data that traditional single-machine tools cannot process efficiently within the required business time.

It is not defined by a fixed size like 1 TB or 10 TB. It depends on the data volume, processing requirements, and available resources.

---

## Q3. What are the 5 Vs of Big Data?

### Answer

The five characteristics of Big Data are:

- Volume → Amount of data
- Velocity → Speed at which data is generated
- Variety → Different types of data
- Veracity → Data quality and reliability
- Value → Business usefulness of the data

---

## Q4. What is Vertical Scaling?

### Answer

Vertical Scaling means increasing the resources of an existing machine by adding more RAM, CPU, or storage.

Example:

8 GB RAM → 64 GB RAM

---

## Q5. What is Horizontal Scaling?

### Answer

Horizontal Scaling means increasing the system's capacity by adding more machines instead of upgrading one machine.

This is the preferred approach for Big Data systems.

---

## Q6. Why do companies prefer Horizontal Scaling?

### Answer

Because it provides:

- Better scalability
- Lower cost
- Better fault tolerance
- No single point of failure

---

## Q7. What is Hadoop?

### Answer

Hadoop is an open-source framework that stores and processes Big Data across multiple machines.

Its main components are:

- HDFS (Storage)
- MapReduce (Processing)

---

## Q8. What is HDFS?

### Answer

HDFS is Hadoop's distributed storage system.

It splits files into blocks, distributes them across multiple machines, and maintains replicas to prevent data loss.

---

## Q9. What is MapReduce?

### Answer

MapReduce is Hadoop's processing engine.

It processes data in two phases:

- Map Phase
- Reduce Phase

---

## Q10. Why was Apache Spark introduced?

### Answer

Apache Spark was introduced to overcome the performance limitations of MapReduce.

Spark reduces unnecessary disk I/O by keeping intermediate data in memory whenever possible, making processing much faster.

---

# 🟡 Level 2 - Intermediate Questions

## Q11. Is every large dataset considered Big Data?

### Answer

No.

A dataset becomes Big Data only when traditional tools cannot process it efficiently within the required business time.

A 200 GB dataset may be Big Data for one company but not for another.

---

## Q12. Can Spark completely replace Hadoop?

### Answer

No.

Spark is mainly a processing engine.

Hadoop also provides HDFS, which is still widely used for distributed storage.

Many organizations use Spark together with HDFS.

---

## Q13. Why is Spark faster than MapReduce?

### Answer

Spark is faster because it reduces unnecessary disk read and write operations.

It keeps intermediate data in memory whenever possible instead of writing it to disk after every step.

---

## Q14. Does Spark store everything in RAM?

### Answer

No.

Spark tries to keep data in memory.

If memory becomes insufficient, it spills data to disk and continues processing.

---

## Q15. Why does MapReduce become slower?

### Answer

MapReduce writes intermediate results to disk after almost every processing stage.

Frequent disk I/O significantly increases execution time.

---

# 🔴 Level 3 - Thinking Questions

## Q16. Your company processes 20 GB of data every night.

SQL completes the job in 15 minutes.

The business allows 2 hours.

Would you recommend Spark?

### Answer

No.

SQL already satisfies the business requirement.

As a Data Engineer, the goal is to choose the simplest technology that meets the business needs, not the most popular one.

---

## Q17. Your data grows from 20 GB to 2 TB.

SQL now takes 6 hours.

The business requires reports in 45 minutes.

Would you recommend Spark?

### Answer

Yes.

The existing solution no longer satisfies the business requirement.

Spark's distributed processing capabilities make it a better choice.

---

## Q18. If you have enough budget, why not buy one extremely powerful server?

### Answer

Because:

- Hardware has physical limits.
- It is very expensive.
- It creates a single point of failure.
- Future upgrades become difficult.

Using multiple commodity servers provides better scalability and fault tolerance.

---

## Q19. What happens if one machine fails in HDFS?

### Answer

The system continues to work because HDFS stores multiple replicas of each data block.

Another machine containing a replica serves the data.

---

## Q20. As a Data Engineer, what is the first question you ask before choosing Spark?

### Answer

I first ask:

"Can the existing solution meet the business requirement?"

If SQL, Python, or Pandas can process the data within the required time, there is no need to introduce Spark.

Technology should always follow the business requirement.

---

# 🎯 Day 1 Interview Tips

✅ Explain concepts with examples.

✅ Don't memorize definitions.

✅ Explain the problem first, then the solution.

✅ Think like a Data Engineer, not like a student.

Example:

❌ Spark is faster because it uses RAM.

✅ Spark is faster because it reduces unnecessary disk I/O by keeping intermediate data in memory whenever possible.

This answer demonstrates deeper understanding.

---

# ⭐ Frequently Asked Follow-up Questions

These are the questions interviewers usually ask after your first answer.

The goal is to test your understanding, not your memory.

====================================================================

## Follow-up 1

### Interviewer

You said Distributed Computing is faster.

**Why is it faster?**

### Expected Answer

Because the work is divided among multiple machines and processed simultaneously (parallel processing).

Instead of one machine processing 100 GB, ten machines can each process 10 GB at the same time.

---

## Follow-up 2

### Interviewer

Can we solve every problem using Distributed Computing?

### Expected Answer

No.

Distributed Computing introduces additional complexity and resource management.

If SQL, Python or Pandas can process the data efficiently within the business deadline, using Distributed Computing is unnecessary.

Choose the simplest solution that satisfies the business requirement.

====================================================================

## Follow-up 3

### Interviewer

How do you decide whether data is Big Data?

### Expected Answer

I don't decide based on the file size.

First I ask:

- Can SQL process it?
- Can Pandas process it?
- Can Python process it?
- Can traditional tools complete it within the required business time?

If the answer is No, then I consider it a Big Data problem.

====================================================================

## Follow-up 4

### Interviewer

Which V of Big Data do you think is the most important?

### Expected Answer

All five are important, but from a Data Engineer's perspective, **Value** is critical.

Processing hundreds of terabytes of data has no benefit unless it provides useful business insights.

The goal is not just to process data but to create business value.

====================================================================

## Follow-up 5

### Interviewer

If your company has enough budget, why not buy one extremely powerful server?

### Expected Answer

Because:

- Hardware has physical limits.
- Future upgrades become difficult.
- It creates a single point of failure.
- Maintenance costs are higher.
- Multiple commodity servers provide better scalability and fault tolerance.

====================================================================

## Follow-up 6

### Interviewer

If one machine fails in a Hadoop cluster, what happens?

### Expected Answer

The cluster continues to work.

HDFS maintains multiple replicas of every data block.

If one machine fails, another machine containing a replica serves the data.

This provides fault tolerance.

====================================================================

## Follow-up 7

### Interviewer

Why do we split files into blocks in HDFS?

### Expected Answer

Splitting files allows multiple machines to store and process different parts of the file simultaneously.

This improves performance and enables distributed processing.

====================================================================

## Follow-up 8

### Interviewer

What is the biggest drawback of MapReduce?

### Expected Answer

MapReduce writes intermediate results to disk after almost every processing stage.

Frequent disk read/write operations increase execution time and reduce performance.

====================================================================

## Follow-up 9

### Interviewer

You said Spark is faster.

**What exactly makes it faster?**

### Expected Answer

Spark reduces unnecessary disk I/O.

It keeps intermediate data in memory whenever possible instead of writing it to disk after every transformation.

This significantly improves processing speed.

====================================================================

## Follow-up 10

### Interviewer

Does Spark always keep data in RAM?

### Expected Answer

No.

Spark tries to keep data in memory.

If memory is insufficient, it automatically spills data to disk and continues processing.

====================================================================

## Follow-up 11

### Interviewer

When would you NOT recommend Spark?

### Expected Answer

If traditional tools such as SQL or Pandas can complete the job within the required business time, I would not recommend Spark.

Using Spark for small workloads adds unnecessary complexity.

====================================================================

## Follow-up 12

### Interviewer

Suppose SQL processes 20 GB of data in 15 minutes.

Business allows 2 hours.

Would you migrate to Spark?

### Expected Answer

No.

The current solution already satisfies the business requirement.

As a Data Engineer, my responsibility is to choose the simplest technology that meets business needs, not the newest technology.

====================================================================

## Follow-up 13

### Interviewer

Suppose the same workload grows to 2 TB and SQL now takes 6 hours.

Business requires the report in 45 minutes.

What would you do?

### Expected Answer

I would evaluate distributed processing using Spark because the current solution no longer satisfies the business SLA.

Spark's parallel processing and reduced disk I/O make it more suitable for large-scale workloads.

====================================================================

## 🎯 Golden Rule for Interviews

Don't answer only **"What?"**

Always explain:

✔ What?

✔ Why?

✔ Example

Example:

Question:

Why is Spark faster?

Bad Answer

"Because it uses RAM."

Good Answer

"Spark reduces unnecessary disk I/O by keeping intermediate data in memory whenever possible. This reduces repeated read/write operations and improves processing speed."

The second answer demonstrates understanding instead of memorization.
