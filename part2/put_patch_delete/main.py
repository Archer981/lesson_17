# У Вас настроенный фласк
# и список словарей с данными.
#
# Вам необходимо:
#
# 1. Создать переменную app c экземпляром
#    класса App из библиотеки flask_restx
#
# 2. Создать неймспейc note_ns с адресом `/notes`
#
# 3. Cоздать Class Based View, который позволяет:
#
# - С помощью PATCH-запроса на адрес `/notes/{id}`
#   частично обновить содержащуюся в в списке
#   сущность с соответствующим id
#
# - С помощью PUT-запроса на адрес `/notes/{id}`
#   перезаписать в списке сущность
#   с соответствующим id
#
# - С помощью DELETE-запроса на адрес `/notes/1`
#   удалить данные о сущности с соответсвующим id

from flask import Flask, request
from flask_restx import Api, Resource
from pprint import pprint

app = Flask(__name__)

api = Api(app)
app.config['RESTX_JSON'] = {'ensure_ascii': False, 'indent': 2}

# api = # TODO допишите код
note_ns = api.namespace('notes') # TODO допишите код

notes = {
    1: {
        "id": 1,
        "text": "this is my super secret note",
        "author": "me"
    },
    2: {
        "id": 2,
        "text": "oh, my note",
        "author": "me"
    }
}

# TODO Допишите Class Based View здесь
@note_ns.route('/<int:uid>')
class NoteView(Resource):
    def put(self, uid):
        data = request.json
        if uid in notes.keys():
            note = notes[uid]
        else:
            return '', 404
        note['text'] = data.get('text')
        note['author'] = data.get('author')
        notes[uid] = note
        return '', 204



    def patch(self, uid):
        data = request.json
        if uid not in notes.keys():
            return '', 404
        else:
            note = notes[uid]
        if data.get('text'):
            note['text'] = data.get('text')
        if data.get('author'):
            note['author'] = data.get('author')
        notes[uid] = note
        return '', 204

    def delete(self, uid):
        if uid in notes.keys():
            del notes[uid]
            return '', 204
        else:
            return '', 404


PUT = {"text": "New note 2", "author": "me"}
PATCH = {"text": "Patched note"}


# # # # # # # # # # # #                                    
if __name__ == '__main__':
    client = app.test_client()                          # TODO вы можете раскомментировать
    # response = client.put('/notes/1', json=PUT)       # соответсвующе функции и
    # response = client.patch('/notes/1', json=PATCH)   # воспользоваться ими для самопроверки
    # response = client.delete('/notes/1')              # аналогично заданию `post`
    pprint(notes, indent=2)
