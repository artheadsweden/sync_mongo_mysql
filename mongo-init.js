db = db.getSiblingDB('db');

db.createCollection('counters');

db.counters.insertOne(
 {
    _id: 'auto_1',
    sequence_value: 50000,
  });