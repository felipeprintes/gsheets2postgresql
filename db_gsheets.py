import app
from sqlalchemy import *

#Conexão com o banco postgresql
engine = create_engine("postgresql://postgres:postgres@localhost/gsheets", echo=True)

metadata = MetaData()

gsheets = Table('gsheets', metadata,
                Column('id', Integer, Sequence('usuario_id_seq'), primary_key=True),
                Column('nome', String),
                Column('idade', Integer),
                Column('curso', String),
                )
metadata.create_all(engine)

results_from_gsheets = app.main()

result = 1
vet_intert=[]
conn = engine.connect()

while result<len(results_from_gsheets):
    conn.execute(gsheets.insert(),
                 [
                    {"nome":results_from_gsheets[result][0],
                    "idade":results_from_gsheets[result][1],
                    "curso":results_from_gsheets[result][2]},
                 ])
    result+=1




#conn.execute(gsheets.insert(), vet_intert)