# Extract hyracks job graph

* Run the following command to extract the edge list of the Hyracks job graph.\
**Input:** JSON representation of hyracks jobs.\
**Output:** edge list in CSV format
```python
python extract_hyracks_jobs_graph.py spatial_join_hyracks_jobs.json edges.csv
```

* Copy and paste the edge list to this online graph editor: https://csacademy.com/app/graph_editor/ \
Check the "Directed" option if needed. Then you can see the graph representation of Hyracks jobs. 
