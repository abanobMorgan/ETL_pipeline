# ETL pipelines 
## Build an ETL Pipeline using Airflow

### Scenario
we are a data engineer at a data analytics consulting company. we have been assigned to a project that aims to de-congest the national highways by analyzing the road traffic data from different toll plazas. Each highway is operated by a different toll operator with a different IT setup that uses different file formats. our job is to collect data available in different formats and consolidate it into a single file.

### Objectives
Building Apache Airflow DAG that will:

+ Extract data from a csv file
+ Extract data from a tsv file
+ Extract data from a fixed width file
+ Transform the data
+ Load the transformed data into the staging area  

### Prepare the environment
+ Start Apache Airflow.  
   + using the command start_airflow
+ Download the dataset from the source to the destination mentioned below.
    * from the source here : https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Final%20Assignment/tolldata.tgz
    ![wget.png](attachment:wget.png)

    #### 1. Create a DAG
<img src="/AirFlow/images/1.dag_args.jpg"/>   

#### 2. Define the DAG
<img src="/AirFlow/images/2.Define_dag.jpg"/>  

#### 3. Create a task to unzip data
<img src="/AirFlow/images/3.unzip_data.jpg"/>  

#### 4. Create a task to extract data from csv file  
<img src="/AirFlow/images/4.extract_data_from_csv.jpg"/>  

#### 5. Create a task to extract data from tsv file  
<img src="/AirFlow/images/5.extract_data_from_tsv.jpg"/>  

#### 6. Create a task to extract data from fixed width file  
<img src="/AirFlow/images/6.extract_data_from_fixed_width.jpg"/>  

#### 7. Create a task to consolidate data extracted from previous tasks  
<img src="/AirFlow/images/7.consolidate_data.jpg"/>  

#### 8. Transform and load the data  
<img src="/AirFlow/images/8.transform.jpg"/>  

#### 9. Define the task pipeline  
<img src="/AirFlow/images/9.task_pipeline.jpg"/>  

#### 10. The pipeline in Airflow UI  
<img src="/AirFlow/images/10.dag_runs.jpg"/>  



