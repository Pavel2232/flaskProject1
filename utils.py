import json

from config import DATA_DIR
from models import *
from flask_set import db

USER_DATA = DATA_DIR.joinpath('user.json')

OFFERS_DATA = DATA_DIR.joinpath('offers.json')


def insert_data_user(input_data):
    """Загрузка пользователей списка в таблицу"""
    for row in input_data:
        db.session.add(User(
            id=row.get("id"),
            first_name=row.get("first_name"),
            last_name=row.get("last_name"),
            age=row.get("age"),
            email=row.get("email"),
            role=row.get("role"),
            phone=row.get("phone")
        ))
        db.session.commit()


def insert_data_order(input_data):
    """Загрузка заказов списка в таблицу"""
    for row in input_data:
        db.session.add(Order(
            id=row.get("id"),
            name=row.get("name"),
            description=row.get("description"),
            start_date=row.get("start_date"),
            end_date=row.get("end_date"),
            address=row.get("address"),
            price=row.get("price"),
            customer_id=row.get("customer_id"),
            executor_id=row.get("executor_id")
        ))
        db.session.commit()


def insert_data_offer(input_data):
    """Загрузка офферов списка в таблицу"""
    for row in input_data:
        db.session.add(Offer(
            id=row.get("id"),
            order_id=row.get("order_id"),
            executor_id=row.get("executor_id")
        ))
        db.session.commit()


def init_db():
    """Заполненин базы данных"""
    with open(USER_DATA, encoding="utf-8") as f:
        insert_data_user(json.load(f))

    with open('data/orders.json', encoding="utf-8") as f:
        insert_data_order(json.load(f))

    with open(OFFERS_DATA, encoding="utf-8") as f:
        insert_data_offer(json.load(f))


def get_all(model):
    """Получааем список таблицы"""
    list = []
    result = db.session.query(model).all()
    for i in result:
        list.append(i.to_dict())
    return list


def get_by_id(model, id):
    """Получаем значение по id"""
    for row in get_all(model):
        if id == row["id"]:
            return row


def add_bd(model, row):
    """Добавить данные в бд"""
    result = model(row)
    db.session.add(result)
    db.session.commit()


def update_bd(model, row, id):
    """Обновить данные в бд"""
    result = model.query.get(id)
    result.all = row
    db.session.add(result)
    db.session.commit()


def delete_bd(model, id):
    """Удалить данные в бд"""
    result = model.query.get(id)
    db.session.delete(result)
    db.session.commit()
