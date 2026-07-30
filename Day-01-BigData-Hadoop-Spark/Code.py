"""
==========================================================
PySpark Industry Roadmap
Day 1 - Environment Preparation
Author : Siva Rama Krishna
==========================================================

Today's Goal
------------
Before writing our first Spark program, let's verify that
our development environment is ready.

Remember:

PySpark is written in Python,
but Apache Spark itself runs on the JVM.

That's why Java is required.

==========================================================
"""

# ==========================================================
# 1. Verify Python Installation
# ==========================================================

import sys

print("=" * 60)
print("Checking Python Installation")
print("=" * 60)

print("Python Version :", sys.version)

"""
Expected Output

Python Version : 3.x.x

Why?

PySpark provides Python APIs,
so Python must be installed.
"""

# ==========================================================
# 2. Verify Java Installation
# ==========================================================

"""
Open Command Prompt and run:

java -version

Expected Output

java version "17"

(or any supported version)

Why?

Spark is written in Scala.

Scala runs on the JVM.

JVM requires Java.

Even though we write PySpark code,

internally Spark executes on Java.
"""

# ==========================================================
# 3. Verify PySpark Installation
# ==========================================================

"""
Open Command Prompt

Run

pyspark --version

Expected Output

Spark Version
Scala Version
Java Version

If this command works,

PySpark has been installed successfully.
"""

# ==========================================================
# 4. Understanding the Execution Flow
# ==========================================================

"""
You write

↓

Python Code

↓

PySpark API

↓

Spark Engine

↓

JVM

↓

Cluster

↓

Result

Important

You DO NOT need to write Java code.

PySpark automatically communicates with Spark through
the JVM using Py4J.

This is why Java must be installed even though
we only write Python code.
"""

# ==========================================================
# 5. Small Revision
# ==========================================================

print("\n")
print("=" * 60)
print("DAY 1 QUICK REVISION")
print("=" * 60)

revision = [
    "✔ Distributed Computing = Multiple machines working together",
    "✔ Big Data = Traditional tools become inefficient",
    "✔ Hadoop = Distributed Storage + Processing",
    "✔ HDFS = Distributed Storage",
    "✔ MapReduce = Processing Engine",
    "✔ Spark = Faster Processing Engine",
    "✔ Spark is faster because it reduces Disk I/O",
]

for point in revision:
    print(point)

print("=" * 60)

"""
End of Day 1

Tomorrow:

We will create our first SparkSession and
understand Spark Architecture.
"""
