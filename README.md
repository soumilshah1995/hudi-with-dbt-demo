
hudi-with dbt-demo

<img width="951" alt="Capture" src="https://user-images.githubusercontent.com/39345855/209361428-2c684510-8d15-48b7-9a78-13a3aa7402eb.PNG">


# Steps 
### Step1 : Deploy the Stack and get IAM Role as shown in video 

* cd Infra
```
npx serverless config credentials --provider aws --key <ACCESS KEY GOES HERE>  --secret <SECRET KEY > -o
  
npx sls deploy
```
 
 ![image](https://user-images.githubusercontent.com/39345855/209359135-b9585ddf-ef0c-4a81-b574-4af6c5380c58.png)

     
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


### Step5 : Go inside dbt-glue and issue commands
```

dbt debug --profiles-dir profile

dbt run
```

### Happy Learning
