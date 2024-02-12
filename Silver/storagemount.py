# Databricks notebook source
configs = {
  'fs.azure.account.key.lreddydatalakegen2.dfs.core.windows.net':'0bjdSXpy8MY8Y8IJ/c+/Uuj4Fhk3le5ZvUI+KX03IJKLz6mdnRMzH87b6ftqCq4eg7y6Yf3qqdrJ+ASt4eeg7g=='
}

# Optionally, you can add <directory-name> to the source URI of your mount point.
dbutils.fs.mount(
  source = "wasbs://bronze@lreddydatalakegen2.blob.core.windows.net/",
  mount_point = "/mnt/bronze",
  extra_configs = {
  'fs.azure.account.key.lreddydatalakegen2.blob.core.windows.net':'0bjdSXpy8MY8Y8IJ/c+/Uuj4Fhk3le5ZvUI+KX03IJKLz6mdnRMzH87b6ftqCq4eg7y6Yf3qqdrJ+ASt4eeg7g=='
})

# COMMAND ----------

    dbutils.fs.ls("/mnt/bronze/SalesLT")

# COMMAND ----------


