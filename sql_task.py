from sqlalchemy import create_engine, Column, String, Integer, Float
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.sql import func

# Создаем подключение к базе данных
engine = create_engine('sqlite:///data.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Определяем модель таблицы
class Table(Base):
    __tablename__ = 'table'
    id = Column(Integer, primary_key=True)
    attr_name = Column(String)
    attr_value = Column(Integer)

# Создаем таблицу
Base.metadata.create_all(bind=engine)

# Входные данные
input_data = [
    {'attr_name': 'name1', 'attr_value': 10},
    {'attr_name': 'name1', 'attr_value': 20},
    {'attr_name': 'name1', 'attr_value': 30},
    {'attr_name': 'name1', 'attr_value': 40},
    {'attr_name': 'name2', 'attr_value': 5},
    {'attr_name': 'name2', 'attr_value': 15},
    {'attr_name': 'name2', 'attr_value': 25},
    {'attr_name': 'name3', 'attr_value': 100},
    {'attr_name': 'name3', 'attr_value': 200},
    {'attr_name': 'name3', 'attr_value': 300},
    {'attr_name': 'name3', 'attr_value': 400},
]

# Заполняем таблицу
for data in input_data:
    row = Table(attr_name=data['attr_name'], attr_value=data['attr_value'])
    session.add(row)
session.commit()

# Запрос для выборки данных
subquery = session.query(Table.attr_name, func.max(Table.attr_value).label('max_value')).group_by(Table.attr_name).subquery()
query = session.query(Table.attr_name, Table.attr_value).join(subquery, Table.attr_name == subquery.c.attr_name).filter(Table.attr_value == subquery.c.max_value)

# Получаем результаты
results = query.all()

# Создаем таблицу для хранения результатов
class Result(Base):
    __tablename__ = 'result'
    id = Column(Integer, primary_key=True)
    attr_name = Column(String)
    avg_value = Column(Float)
    min_value = Column(Integer)
    max_value = Column(Float)

# Создаем таблицу
Base.metadata.create_all(bind=engine)

# Вычисляем среднее, минимальное и максимальное значения attr_value для каждого attr_name
for attr_name, attr_value in results:
    avg_value = session.query(func.avg(Table.attr_value)).filter(Table.attr_name == attr_name).scalar()
    min_value = session.query(func.min(Table.attr_value)).filter(Table.attr_name == attr_name).scalar()
    max_value = session.query(func.max(Table.attr_value)).filter(Table.attr_name == attr_name).scalar()
    row = Result(attr_name=attr_name, avg_value=avg_value, min_value=min_value, max_value=max_value)
    session.add(row)
session.commit()

# Запрос для выборки данных
query = session.query(Result)

# Получаем результаты
final_results = query.all()

# Выводим результаты
for result in final_results:
    print(f"id: {result.id}, attr_name: {result.attr_name}, avg_value: {result.avg_value}, min_value: {result.min_value}, max_value: {result.max_value}")
