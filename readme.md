# ETL pipelines 

1. [Build an ETL Pipeline using Airflow](#AirFlow)
    1. [Scenario](#Scenario)
    2. [Objectives](#Objectives)
    3. [Prepare the environment](#environment)
    4. [Build the Ariflow DAG](#DAG)
    
2. [Creating Streaming Data Pipelines using Kafka](#Kafka)   
    1. [Scenario](#scen)
    2. [Objectives](#obj)
    3. [Prepare the environment](#env)
    4. [Building Kafka](#Kafka)


<a name="AirFlow"></a>
## Build an ETL Pipeline using Airflow 


<a name="Scenario"></a>
### Scenario
we are a data engineer at a data analytics consulting company. we have been assigned to a project that aims to de-congest the national highways by analyzing the road traffic data from different toll plazas. Each highway is operated by a different toll operator with a different IT setup that uses different file formats. our job is to collect data available in different formats and consolidate it into a single file.
<a name="Objectives"></a>
### Objectives
Building Apache Airflow DAG that will:

+ Extract data from a csv file
+ Extract data from a tsv file
+ Extract data from a fixed width file
+ Transform the data
+ Load the transformed data into the staging area  

<a name="environment"></a>
### Prepare the environment
+ Start Apache Airflow.  
   + using the command start_airflow
+ Download the dataset from the source to the destination mentioned below.
    * from the source here : https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Final%20Assignment/tolldata.tgz
    ![wget.png](attachment:wget.png)

    <a name="DAG"></a>

### Build the Ariflow DAG
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



<a name="Kafka"></a>
## Creating Streaming Data Pipelines using Kafka

<a name="scen"></a>

### Scenario
we are a data engineer at a data analytics consulting company. we have been assigned to a project that aims to de-congest the national highways by analyzing the road traffic data from different toll plazas. As a vehicle passes a toll plaza, the vehicle's data like vehicle_id,vehicle_type,toll_plaza_id and timestamp are streamed to Kafka. our job is to create a data pipe line that collects the streaming data and loads it into a database.

<a name="obj"></a>
### Objectives
Building a streaming data pipe by performing these steps:

+ Start a MySQL Database server.
+ Create a table to hold the toll data.
+ Start the Kafka server.
+ Install the Kafka python driver.
+ Install the MySQL python driver.
+ Create a topic named toll in kafka.
+ Download streaming data generator program.
+ Customize the generator program to steam to toll topic.
+ Download and customise streaming data consumer.
+ Customize the consumer program to write into a MySQL database table.
+ Verify that streamed data is being collected in the database table.

<a name="env"></a>

### Prepare the environment

* download the:--> kafka:` wget https://archive.apache.org/dist/kafka/2.8.0/kafka_2.12-2.8.0.tgz`
* Extract Kafka:--> `tar -xzf kafka_2.12-2.8.0.tgz`
* start MySQL data base:--> `start_mysql`
* Connect to the mysql server:--> `mysql --host=127.0.0.1 --port=3306 --user=root --password= ******` 
* Create a database named tolldata:--> `create database tolldata;`
* Create a table named livetolldata:-->   
    `use tolldata;  
    create table livetolldata(timestamp datetime,vehicle_id int,vehicle_type char(15),toll_plaza_id smallint);`
* Disconnect from MySQL server:--> `exit`
* Install the python module kafka-python:--> `pip3 install kafka-python`
* Install the python module mysql-connector-python:--> `pip3 install mysql-connector-python`

### Building Kafka  
<a name="Kafka"></a>

#### 1. Start Zookeeper
<img src="/Kafka/images/1.start_zookeeper.jpg"/>  

#### 2. Start Kafka server
<img src="/Kafka/images/2.start_kafka.jpg"/>  

#### 3. Create a topic named toll
<img src="/Kafka/images/3.create_toll_topic.jpg"/>  

#### 4. Create Toll Traffic Simulator
<img src="/Kafka/images/4.Create_Toll_Traffic_Simulator.jpg"/>  

#### 5. Run the Toll Traffic Simulator
<img src="/Kafka/images/5.simulator_output.jpg"/>  

#### 6. Create streaming_data_reader.py
<img src="/Kafka/images/6.Create_streaming_data_reader.py.jpg"/>  

#### 7. Run streaming_data_reader.py
<img src="/Kafka/images/7.data_reader_output.jpg"/>  
