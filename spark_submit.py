# Databricks notebook source
x=5
y=10    
m = x*y
print(m)
print(m+2)

# COMMAND ----------

spark submit
driver node
DAG scheduler
cluster manager
worker node

# COMMAND ----------

general purpose worker node - dev activity 
memory optimized- used for complex joins/transformation
storage optimized - simple ETL ops 

# COMMAND ----------

import pyspark

# COMMAND ----------

from pyspark import SparkContext

# COMMAND ----------

sc = SparkContext('new','Geek_demo')

# COMMAND ----------

rdd = sc.parallelize(([1,2,3],[4,1,43],[3,48,12],[6,9,1]))

# COMMAND ----------

rdd.collect()

# COMMAND ----------

rdd.count()

# COMMAND ----------

rdd.map(lambda x : (x*2)).collect()

# COMMAND ----------

rdd.flatMap(lambda x : (x*2)).collect()

# COMMAND ----------

rdd.getNumPartitions()

# COMMAND ----------

sparksession = sparkcontext + sqlcontext
