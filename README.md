## This project is a proof of concept
What we are trying to achive here is avoiding a conflict of auto incremented values in a MySQL database and a MongoDB.


#### MySQL
We achive this by letting the the MySQL database use either odd or even numbers when auto incrementing.

This can be done by setting

```sql
SET GLOBAL auto_increment_increment = 2;
```
Note: I have not got this to work without the GLOBAL flag, when initializing from the docker-compose file.

This will increment by 2 each time.
We can also set the starting value for the increment with:

```sql
ALTER TABLE table_name AUTO_INCREMENT = 3001;
```

#### MongoDB
As MongoDB does not have an auto increment feature we will need to achive one by ourselvs.

First we create a collection in our Mongo database. Here it is hard coded to be named counters.

Each document in this collection will handle one auto increment counter. The structure for a document here is:
```json
{
    "_id": "name_of_counter",
    "sequence_value": 101
}
```

The _id field is given a value that will be the name that we use for this counter.

The secuence_value will keep track of where we are in the auto increment for this counter. Initially it can be set to one step below the first value we want to use. In the example above, the first value used will be 103 (if we increase by 2).

From the Python side we can use a function that looks something like the _get_auto_id method in the Document class. You can find it in the mongo_doc module. This method returns the next value to be used. 

You can now create the data you want to store as a dict:

```python
data = {
    'name': 'Anna',
    'age': 33,
    'auto_id': _get_auto_id('auto_1')
}
```

Here we are using a document from the coutners collection with _id = auto_1.

In the example project this call will be handled by the save method in the document class.

This way of manageing the auto increment value will ensure that all values will be unique as long as the sequence_value in the counters collection is not tampered with.

### Conclusion
As we are using two separate intervals for the auto increments we will ensure that they never collide. This is a rather simple solution that will let us handle the problem without any use of a middleware software that will sync or generate id's.