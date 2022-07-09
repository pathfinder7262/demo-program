import pymongo

conn = pymongo.MongoClient("mongodb://localhost:27017/")
db = conn["college"]    #DB created
col = db['student']      #collection created / Table created
print(conn)
print(col)
print(db)

#insert data

stu_rec = [
    {'rno':101,'name':'chetan','course':'python'},
    {'rno':102,'name':'ketan','course':'python'},
    {'rno':103,'name':'pk','course':'python'},
    {'rno':104,'name':'manish','course':'python'},
    {'rno':105,'name':'akki','course':'python'},
    {'rno':106,'name':'swap','course':'python'},
    {'rno':107,'name':'mange','course':'python'},
    {'rno':108,'name':'paresh','course':'python'},
    {'rno':109,'name':'mano','course':'python'},
    {'rno':110,'name':'somya','course':'python'},
    {'rno':111,'name':'rohit','course':'python'},
    {'rno':112,'name':'arjun','course':'python'},
    {'rno':113,'name':'ram','course':'python'},
    {'rno':114,'name':'sham','course':'python'},
    ]

x = col.insert_many(stu_rec)

#print list of the _id values of the inserted document:
print(x.inserted_ids)
print(len(x.inserted_ids))
