### 1) Clone repo
```
git clone https://github.com/bohdanlesiv/GL-task.git

``` 

###2) Go to folder homework 3 and create folder data
```
 cd GL-task/homework3/
 sudo mkdir data

```
###3) Copy file from google bucket to the local (data directory)

```
gsutil cp gs://{put bucket here}/ .
```

###4) Create HDFS directory
```
hdfs dfs -mkdir -p /bdpc/hadoop_mr/avg_top/input
```

###5) Copy file data/flights.csv.zip to hdfs
```
hdfs dfs -copyFromLocal data/flights.csv.zip /bdpc/hadoop_mr/avg_top/input
```
###6) Run the first app ( top 5 avg delay by each airport) path \homework3\airport_avg_top
```
 sudo ./submit_avg_top.sh 
```
###7) Copy file data/flights.csv.zip to hdfs in order to run task for data merging
```
hdfs dfs  -copyFromLocal data/airports.csv /bdpc/hadoop_mr/avg_top/output
```
###8). go to cataloge homework3\airport_join (apply join for two datasets )
```
 sudo ./submit_join.sh
```
