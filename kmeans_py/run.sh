HADOOP_CMD="/opt/hadoop/bin/hadoop"
STREAM_JAR_PATH="/opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.6.jar"
    
INPUT_FILE_PATH="/kmeans_py/data.csv"
OUTPUT_PATH="/kmeans_py/output"
    
$HADOOP_CMD fs -rm -r  $OUTPUT_PATH 
    
$HADOOP_CMD jar $STREAM_JAR_PATH \
    -input $INPUT_FILE_PATH \
    -output $OUTPUT_PATH \
    -mapper "python map.py" \
    -reducer "python reduce.py" \
    -file ./map.py \
    -file ./reduce.py
