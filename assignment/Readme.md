Assesment: Do reseach on MapReduce

count how many AI companies there are in each country
make a top 10 countries with most AI companies
How many companies are from the Netherlands
Code has to run on HDFS with a basic setup
Code is executed with a python command with MrJob

Hadoop system MapReduce
----------------------------------------------------------------
- i first converted my excell file to a csv file whitch was more easy to handle

- i then wrote the scripts using chatgpt, and trying stuff out, using the example from the slides and looking online.

- i put my scripts in the hdfs in maria_dev/ai
- i put my data in the hdfs in maria_dev/ai/input

- i made an ssh connection to the cluster using putty:
host name : maria_dev@127.0.0.1
Port : 2222 (do not use 22) 
Saved sessions : HDP 
----------------------------------------------------------------
------i got the scripts and the data from hdfs:
hdfs dfs -get hdfs:///user/maria_dev/ai/input/AI.csv AI.csv

hdfs dfs -get hdfs:///user/maria_dev/ai/count_countries.py count_countries.py;
hdfs dfs -get hdfs:///user/maria_dev/ai/count_netherlands.py count_netherlands.py;
hdfs dfs -get hdfs:///user/maria_dev/ai/top_10_countries.py top_10_countries.py;
----------------------------------------------------------------
------i exectued them using, storing the output in a file:
python count_countries.py AI.csv > count_countries.txt;
python top_10_countries.py AI.csv > top_10_countries.txt;
python count_netherlands.py AI.csv > count_netherlands.txt;

or using (if i wanted to use all the available nodes in hadoob):

python count_countries.py -r hadoop --hadoop-streaming-jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar AI.csv > count_countries.txt;
python top_10_countries.py -r hadoop --hadoop-streaming-jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar AI.csv > top_10_countries.txt;
python count_netherlands.py -r hadoop --hadoop-streaming-jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar AI.csv > count_netherlands.txt;

----------------------------------------------------------------
------i put the output in the hdfs by doing:
hdfs dfs -put count_countries.txt hdfs:///user/maria_dev/ai/output;
hdfs dfs -put top_10_countries.txt hdfs:///user/maria_dev/ai/output;
hdfs dfs -put count_netherlands.txt hdfs:///user/maria_dev/ai/output;

----------------------------------------------------------------
------i cleaned up the system
rm count_countries.txt;
rm count_netherlands.txt;
rm top_10_countries.txt;
rm count_countries.py;
rm count_netherlands.py;
rm top_10_countries.py;
rm AI.csv;

my scripts are available in github:
...
