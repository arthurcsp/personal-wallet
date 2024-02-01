from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import registry
from src.domain.models.registers import Category

mapper_registry = registry()

category_table = Table(
    "category",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(200)),
    Column("subcategory", String(200)),
    Column("group", String(200))
    )




mapper_registry.map_imperatively(Category, category_table)