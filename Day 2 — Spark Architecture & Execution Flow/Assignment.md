# Day 2 - Assignment

---

# Objective

The objective of this assignment is to test your understanding of Spark Architecture and develop the thinking process of a Data Engineer.

Do not search for answers on the internet.

Try to answer based on your understanding.

---

# Part 1 - Theory Questions

## Question 1

Draw the complete Spark Architecture and explain the responsibility of each component.

Your diagram should include:

- Spark Application
- Driver
- Cluster Manager
- Worker Nodes
- Executors
- Tasks

---

## Question 2

Why is the Driver called the Brain of the Spark Application?

Explain using a real-time example.

---

## Question 3

Differentiate between a Worker Node and an Executor.

Explain their responsibilities in your own words.

---

## Question 4

Why doesn't the Driver process the entire dataset by itself?

What is the advantage of allowing Executors to process the data instead?

---

## Question 5

Explain the responsibility of the Cluster Manager.

What would happen if there were no Cluster Manager?

---

# Part 2 - Scenario Based Questions

## Scenario 1

A Spark job is processing 500 GB of data.

The Driver is running successfully.

Executors are processing the data.

Suddenly one Executor fails.

### Questions

- Will the Driver stop?
- Will the Spark Application immediately fail?
- What will Spark try to do?

Explain your answer.

---

## Scenario 2

The Driver suddenly crashes while processing a Spark job.

### Questions

- Can Executors continue working?
- Why or why not?
- Why is Driver failure considered more serious than Executor failure?

---

## Scenario 3

One Worker Node is using 90% CPU while the remaining Worker Nodes are almost idle.

### Questions

Would your first recommendation be:

"Let's add more Worker Nodes."

OR

Would you investigate first?

If you investigate, what things would you check?

---

## Scenario 4

Your manager says:

"Our Spark job is slow.

Let's add five more Worker Nodes."

How would you respond as a Senior Data Engineer?

Explain your thought process.

---

# Part 3 - Senior Engineer Thinking

Answer the following questions.

## Question 1

What is the first thing you investigate when a Spark job becomes slow?

---

## Question 2

Why shouldn't a Data Engineer immediately blame the Worker Nodes?

---

## Question 3

How can uneven task distribution affect Spark performance?

---

## Question 4

What is Data Skew?

Why can it slow down a Spark job?

---

## Question 5

When is adding more Worker Nodes actually a good solution?

---

# Part 4 - Architecture Recall

Without looking at your notes, write the complete Spark Architecture.

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

Now explain each component in one sentence.

---

# Part 5 - Reflection

Write short answers for the following questions.

1. What new concepts did I learn today?

2. Which topic was the most difficult?

3. Which topic do I understand the best?

4. If I were explaining Spark Architecture to a friend, how would I explain it?

5. What mistakes did I make while learning today?

---

# Self Evaluation

Rate yourself out of 10.

| Topic | Rating (/10) |
|--------|--------------|
| Spark Architecture | |
| Driver | |
| Cluster Manager | |
| Worker Nodes | |
| Executors | |
| Tasks | |
| Driver vs Executor | |
| Worker Node vs Executor | |
| Senior Engineer Thinking | |
| Overall Confidence | |

---

# Success Criteria

You have successfully completed Day 2 if you can:

- Explain the complete Spark Architecture without referring to notes.
- Explain the role of every component.
- Differentiate Driver, Worker Node, Executor and Cluster Manager.
- Explain why Driver failure is more serious than Executor failure.
- Think like a Senior Data Engineer before suggesting scaling.
- Explain Data Skew and uneven task distribution using real-time examples.
- Confidently answer the Day 2 interview questions without hesitation.
