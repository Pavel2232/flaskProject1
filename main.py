from flask import jsonify, request
from flask_set import app
from models import User, Offer, Order
from utils import init_db, get_all, get_by_id, add_bd, update_bd, delete_bd


@app.route("/users")
def users_page():
    """Страница всех пользователей"""
    return jsonify(get_all(User))


@app.route("/users", methods=['POST'])
def users_page_upload():
    """Создание  пользователя"""
    content = request.form['content']
    result = add_bd(User, content)
    return "Пользователь создан"


@app.route("/user/<int:id>")
def user_page(id):
    """Страница 1 пользователя по id"""
    return jsonify(get_by_id(User, id))


@app.route("/user/<int:id>", methods=['PUT'])
def user_update(id):
    """Страница обновления пользователя"""
    content = request.form['content']
    result = update_bd(User, content, id)
    return "Пользователь обновлён"


@app.route("/user/<int:id>", methods=['DELETE'])
def user_delete(id):
    """Страница удаления пользователя"""
    delete_bd(User, id)
    return "Пользователь обновлён"


@app.route("/orders")
def orders_page():
    """Страница всех заказов"""
    return jsonify(get_all(Order))


@app.route("/orders", methods=['POST'])
def orders_page_upload():
    """Создание  заказа"""
    content = request.form['content']
    result = add_bd(Order, content)
    return "Заказ создан"


@app.route("/order/<int:id>")
def order_page(id):
    """Страница 1 заказа по id"""
    return jsonify(get_by_id(Order, id))


@app.route("/order/<int:id>", methods=['PUT'])
def order_update(id):
    """Страница обновления заказа"""
    content = request.form['content']
    result = update_bd(Order, content, id)
    return "Заказ обновлён"


@app.route("/order/<int:id>", methods=['DELETE'])
def order_delete(id):
    """Страница удаления заказа"""
    delete_bd(Order, id)
    return "Заказ удалён"


@app.route("/offers")
def offers_page():
    """Страница 1 приглашения по id"""
    return jsonify(get_all(Offer))


@app.route("/offers", methods=['POST'])
def offers_page_upload():
    """Создание  приглашения"""
    content = request.form['content']
    result = add_bd(Offer, content)
    return "Приглашение создано"


@app.route("/offer/<int:id>")
def offer_page(id):
    """Страница 1 заказа по id"""
    return jsonify(get_by_id(Offer, id))


@app.route("/offer/<int:id>", methods=['PUT'])
def offer_update(id):
    """Страница обновления приглашения"""
    content = request.form['content']
    result = update_bd(Offer, content, id)
    return "Приглашен и обновлён"


@app.route("/offer/<int:id>", methods=['DELETE'])
def offer_delete(id):
    """Страница удаления приглашения"""
    delete_bd(Offer, id)
    return "приглашение удалено"


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=80, debug=True)
