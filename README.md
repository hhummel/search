# search

This repo explores how to architect a data structure to enable rapid search of a large data set. The assumptions are:

- The data consists of a set of entities that are assumed completely described by their data fields, which is to stay IID (independent and identically distributed).

- Each entity could have any of a finite number of data sources describing it.

- The schema for each data source is fixed, and consists of a few string values but mostly booleans.

- Queries are made using only the boolean fields. String fields are only for labeling. If a multivalued field is needed for a query, it can be implemented using a one-hot approach.

- The goal is to determine cardinality, not to return the actual data. Further processing could be allowed as a follow-on, asynchronous step.

- It's acceptable to return estimates of the cardinality, so long as the estimates can be improved if necessary with additional resources.

- It's acceptable to have a slow batch processing step to enable the fast searching.

The strategy used in this exploration is:

- Store the data as an array of bytearrays, one for each entity. The bytearrays represent an encoding for each data source and each field in the datasource's fixed schema. Each bytearray has the same schema.

- The bytearrays could get pretty large if there are lots of data sources and lots of fields. Processing time for a bit operations on a bytearray of length N scale like log(N).

- I assume queries can be implemented as masks and bit operations on the bytearray, and that the operations can be combined into a single one on the bytearray. In practice more than one operation might be needed.

- Because the entities are independent, a sampling of the entities can be used to estimate the cardinality, and the sampling is parallelizable. Naive sampling is the jumping off point, but more sophisticated approaches could improve efficiency.

- The overall processing effort to estimate cardinality of a query on the dataset would scale like S log(N), where S is the needed sample size and N is the length of the bytearray. 

- To give a sense of the processing time, running a bit-wise OR on 1,000,000 bitarrays of 100,000 elements took 10 seconds on a seven year old Macbook Air. Performance falls apart for bitarrays between 100,000 and 1,000,000 bits, perhaps due to hardware limitations.

- Although this code is written in Python, it leverages the bitarray package, that implements the byte arrays and bit operations in C.
 

 