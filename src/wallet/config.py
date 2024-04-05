from sqlalchemy import create_engine, text
from wallet.adapter.orm import start_mapper, mapper_registry

engine = create_engine("sqlite:///movements.db")
mapper_registry.metadata.create_all(engine)

with engine.connect() as connection:
    result = connection.execute(text('select "Hello"'))



    print(result.all())
