# Day 2 - Code

---

# Objective

Day 2 focused on understanding the Spark Architecture.

There is very little coding involved because we first need to understand how Spark works internally before writing PySpark programs.

---

# 1. Import SparkSession

```python
from pyspark.sql import SparkSession
```

### Explanation

We import the `SparkSession` class because it is the entry point to every PySpark application.

Without SparkSession, we cannot start a Spark application.

---

# 2. Create a SparkSession

```python
spark = SparkSession.builder \
    .appName("Day2_SparkArchitecture") \
    .getOrCreate()
```

### Explanation

Here,

- `builder` is used to configure the Spark application.
- `appName()` gives a name to the Spark application.
- `getOrCreate()` creates a new SparkSession if one does not already exist. Otherwise, it returns the existing SparkSession.

---

# 3. Print the SparkSession

```python
print(spark)
```

### Output

```
<pyspark.sql.session.SparkSession object at ...>
```

### Explanation

This confirms that the Spark application has started successfully.

---

# 4. Print Spark Version

```python
print(spark.version)
```

### Example Output

```
4.x.x
```

### Explanation

This displays the version of Apache Spark currently being used.

---

# 5. Stop the Spark Application

```python
spark.stop()
```

### Explanation

This stops the Spark application and releases the resources allocated to it.

---

# Complete Program

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Day2_SparkArchitecture") \
    .getOrCreate()

print(spark)

print(spark.version)

spark.stop()
```

---

# What Happens Internally?

When this program runs, Spark follows this sequence:

```
Python Program
       ↓
Create SparkSession
       ↓
Driver Starts
       ↓
Cluster Manager
       ↓
Worker Nodes
       ↓
Executors
       ↓
Ready to Process Data
```

---

# Key Learning

This program **does not process any data**.

It only initializes the Spark Application.

The actual data processing will begin when we start working with DataFrames and perform Actions in the upcoming days.

---

# Senior Engineer Thinking

A Senior Data Engineer understands that:

- SparkSession is the entry point of every Spark application.
- Creating a SparkSession does **not** mean Spark immediately starts processing data.
- Data processing begins only when we execute Spark operations (especially Actions).

---

# Summary

Today we learned how to:

- Import SparkSession.
- Create a SparkSession.
- Start a Spark application.
- Check the Spark version.
- Stop the Spark application.
- Understand what happens internally when a Spark application starts.
