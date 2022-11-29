from mongo_doc import init_db, create_collection_class
from raw_mysql import RawSql

def test_mongo():
    init_db('mongodb://localhost:27017', 'db')
    DataDoc = create_collection_class('DataDoc', 'data')
    data = {
        'name': 'Filias', 
        'age': 56
    }
    doc = DataDoc(**data)
    doc.save('id', 'auto_1')

    docs = DataDoc.all()
    for d in docs:
        print(d)


def test_mysql():
    sql = RawSql('root', 's3cr37', 'localhost', 3306, 'db')
    sql.store_dict('id_test', {
        'name': 'Fia-Lisa',
        'age': 55
    })
    for row in sql.get_all('id_test'):
        print(row)

def main():
    print('MongoDB')
    print('*' * 40)
    test_mongo()
    print('MySQL')
    print('*' * 40)
    test_mysql()

if __name__ == '__main__':
    main()