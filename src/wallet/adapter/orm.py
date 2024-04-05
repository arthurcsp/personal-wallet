from sqlalchemy import Table, Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import registry
from wallet.models.movements import  Movements
from wallet.models.registers import Category, Account

mapper_registry = registry()

category_table = Table(
    "category",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(200)),
    Column("subcategory", String(200)),
    Column("group", String(200))
    )

account_table = Table(
    "account",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(200)),
    Column("type", String(200)),
    Column("balance", Float)
)

movement_table = Table(
    "movement",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True),
    Column("account", Integer),
    Column("category", Integer),
    Column("amount", Float),
    Column("description", String(200)),
    Column("time", DateTime)
)




def start_mapper():
    mapper_registry.map_imperatively(Category, category_table)
    mapper_registry.map_imperatively(Account , account_table)
    mapper_registry.map_imperatively(Movements, movement_table)