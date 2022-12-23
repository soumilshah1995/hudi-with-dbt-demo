
hudi-with dbt-demo

<img width="951" alt="Capture" src="https://user-images.githubusercontent.com/39345855/209358284-b20be393-b554-4495-b8dc-86e261e759c8.PNG"


# Steps 
### Step1 : Deploy the Stack and get IAM Role as shown in video 
### Step2 : add the settings C:\Users\<USERNAME>\.dbt
```
dbtglue:
  target: dev
  outputs:
    dev:
      project_name : 'dbtglue'
      type: glue
      query-comment: demo
      role_arn: "arn:aws:iam::XXX:role/GlueInteractiveSessionRole"
      region: us-west-2
      workers: 3
      worker_type: G.1X
      schema: "hudidb"
      database: "hudidb"
      session_provisioning_timeout_in_seconds: 300
      location: "s3://sXXXXXX/hudi"
      connections: "hudi-connection"
      conf: "spark.serializer=org.apache.spark.serializer.KryoSerializer"

```
### Step3 : Install the dependencies
```
pip3 install -r requirements.txt
```

### Step4 : Run the glue notebook and insert data into HUdi Raw tables 


### Step5 : Go inside dbtgluen and issue commands
```

dbt debug --profiles-dir profile

dbt run
```

### Happy Learning
