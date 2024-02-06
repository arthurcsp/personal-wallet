from sqlalchemy import create_engine, text
from wallet.adapter.orm import start_mapper, mapper_registry

engine = create_engine("sqlite:///:memory:")
mapper_registry.metadata.create_all(engine)

with engine.connect() as connection:
    result = connection.execute(text('select "Hello Memory"'))
    start_mapper()


    print(result.all())
