# Databricks notebook source
'''data warehousing --structured data --
data lake - structured ,semi, unstructured-- not an ACID compliant
lake house - structured,semi,unstructured--data warehousing + data lake---concept of Databricks
delta lake--storage layer, store data in delta format
file_format - parquet
'''

# COMMAND ----------

from pyspark.sql.types import *
from pyspark.sql.functions import *

# COMMAND ----------

spark.CreateDataFrame([],schema=['name','id']).write.format('delta').save('/FileStore/tables/delta')

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE employees (
# MAGIC     EMPNO STRING,
# MAGIC     ENAME STRING,
# MAGIC     JOB STRING,
# MAGIC     MGR STRING,
# MAGIC     HIREDATE STRING,
# MAGIC     SAL INTEGER,
# MAGIC     COMM INTEGER,
# MAGIC     DEPTNO INTEGER
# MAGIC )
# MAGIC USING DELTA
# MAGIC OPTIONS ('header', 'true')
# MAGIC LOCATION '/Volumes/workspace/default/test_practice/emp.csv'

# COMMAND ----------

# MAGIC %sql
# MAGIC create table emp
# MAGIC using DELTA OPTIONS ('header' 'true') as 
# MAGIC select * from
# MAGIC csv.`/Volumes/workspace/default/test_practice/emp.csv`
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC create table employees 
# MAGIC using DELTA OPTIONS ('header' 'True') LOCATION '/Volumes/workspace/default/test_practice/emp.csv'
# MAGIC

# COMMAND ----------



# COMMAND ----------

spark.read.table('employees').display()

# COMMAND ----------

from delta.tables import DeltaTable

# COMMAND ----------

df_delta = DeltaTable.forName(spark,'employees')


# COMMAND ----------

df_emp = spark.read.option('header',True).table('employees')


# COMMAND ----------

df_emp = df_emp.select(col("_c0").alias('EMPNO'),col("_c1").alias('ENAME'),col("_c2").alias('JOB'),col("_c3").alias('MGR'),col("_c4").alias('HIREDATE'),col("_c5").alias('SAL'),col("_c6").alias('COMM'),col("_c7").alias('DEPTNO')).filter(col('_c5')!='SAL')
df_emp.write.mode('overwrite').option('mergeSchema', True).saveAsTable('employees')

# COMMAND ----------

DeltaTable.forPath(spark,'/Volumes/workspace/default/test_practice/target_data/').toDF().display()

# COMMAND ----------

DeltaTable.isDeltaTable(spark,identifier='/Volumes/workspace/default/test_practice/target_data/')

# COMMAND ----------

df_delta_emp = DeltaTable.forName(spark,'employees')

# COMMAND ----------

df_delta_emp.history().display()

# COMMAND ----------

df_emp.display()

# COMMAND ----------

df_delta_emp.restoreToVersion(0)

# COMMAND ----------

spark.read.option('timestampAsOf','2025-07-19T02:45:26.000+00:00').table('employees').display()

# COMMAND ----------

spark.read.option('versionAsOf','1').table('employees').display()

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE HISTORY employees 

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select * from employees version as of 0

# COMMAND ----------

DeltaTable.convertToDelta()