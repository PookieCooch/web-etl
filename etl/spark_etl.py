import json
from pyspark.sql import SparkSession
from api_client import fetch_api_data
import os

os.environ["PYSPARK_PYTHON"] = r"C:\Users\milin\AppData\Local\Programs\Python\Python311\python.exe"
os.environ["PYSPARK_DRIVER_PYTHON"] = r"C:\Users\milin\AppData\Local\Programs\Python\Python311\python.exe"


def run_etl(url, headers):
    spark = (
        SparkSession.builder
        .appName("simple-web-etl")
        .master("local[*]")
        .getOrCreate()
    )

    data = fetch_api_data(url, headers)

    def normalize(record):
        out = {}
        for k, v in record.items():
            if isinstance(v, (dict, list)):
                out[k] = json.dumps(v)
            else:
                out[k] = v
        return out

    normalized_data = [normalize(r) for r in data]
    
    df = spark.createDataFrame(normalized_data)

    #df = spark.createDataFrame(data)

    df.show(truncate=False)
    df.printSchema()

    #rdd = spark.sparkContext.parallelize([json.dumps(data)])
    #df = spark.read.json(rdd)

    #print(df)

    #df.write \
    #  .mode("overwrite") \
    #  .jdbc(
    #      url="jdbc:postgresql://localhost:5432/etl",
    #      table="api_data",
    #      properties={
    #          "user": "postgres",
    #          "password": "postgres",
    #          "driver": "org.postgresql.Driver"
    #      }
    #  )

    result = {
        "rows": df.count(),
        "schema": df.schema.simpleString()
    }

    spark.stop()
    
    return result

run_etl("https://jsonplaceholder.typicode.com/users",headers={})