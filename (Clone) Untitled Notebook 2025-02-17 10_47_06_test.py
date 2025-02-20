# Databricks notebook source
# MAGIC %sql
# MAGIC select * from samples.tpch.customer

# COMMAND ----------

# MAGIC %sql
# MAGIC create or replace view hive_metastore.default.customer_vw as
# MAGIC select * from samples.tpch.customer

# COMMAND ----------

# MAGIC %sql
# MAGIC create or replace temp view customer_vw as
# MAGIC select * from samples.tpch.customer
# MAGIC where UPPER(c_mktsegment) = 'AUTOMOBILE'
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from customer_vw

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE TABLE samples.tpch.customer

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE customer_mktseg_auto (
# MAGIC     c_custkey BIGINT COMMENT 'Customer Key',
# MAGIC     c_name STRING COMMENT 'Customer Name',
# MAGIC     c_address STRING COMMENT 'Customer Address',
# MAGIC     c_nationkey BIGINT COMMENT 'Nation Key',
# MAGIC     c_phone STRING COMMENT 'Phone Number',
# MAGIC     c_acctbal DECIMAL(18,2) COMMENT 'Account Balance',
# MAGIC     c_mktsegment STRING COMMENT 'Market Segment',
# MAGIC     c_comment STRING COMMENT 'Comment'
# MAGIC )

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC Insert into customer_mktseg_auto
# MAGIC Select * from customer_vw

# COMMAND ----------

# MAGIC %sql
# MAGIC create or replace view hive_metastore.default.customer_vw as
# MAGIC select * from customer_mktseg_auto