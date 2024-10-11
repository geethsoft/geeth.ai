from flask import Blueprint, jsonify

# Define a blueprint for the chat routes
chats = Blueprint('chats', __name__)

from ai.llms.llama_bot import llama_bot

@chats.route('/', ['GET'])
def getChats():
    return jsonify(message="Welcome to the chat home page!")

@chats.route('/', ['POST'])
def createChat():
    return jsonify(message="Welcome to the chat home page!")

@chats.route('/rename/<int:chat_id>', ['PATCH'])
def renameChatByID(chat_id):
    return jsonify(chat_id=chat_id, message="This is a specific chat!")

@chats.route('/archive/<int:chat_id>', ['PATCH'])
def archiveChatByID(chat_id):
    return jsonify(chat_id=chat_id, message="This is a specific chat!")

@chats.route('/<int:chat_id>', ['GET'])
def getChatByID(chat_id):
    return jsonify(chat_id=chat_id, message="This is a specific chat!")

@chats.route('/<int:chat_id>', ['PUT'])
def updateChatByID(chat_id):
    return jsonify(chat_id=chat_id, message="This is a specific chat!")

@chats.route('/<int:chat_id>', ['DELETE'])
def deleteChatByID(chat_id):
    return jsonify(chat_id=chat_id, message="This is a specific chat!")

@chats.route('/<int:chat_id>/messages/<int:message_id>', ['GET'])
def getMessageByID(chat_id):
    return jsonify(chat_id=chat_id, message="This is a specific chat!")

@chats.route('/<int:chat_id>/messages/<int:message_id>', ['DELETE'])
def deleteMessageByID(chat_id):
    return jsonify(chat_id=chat_id, message="This is a specific chat!")

@chats.route('/<int:chat_id>/messages/<int:message_id>', ['PUT'])
def updateMessageID(chat_id):
    return jsonify(chat_id=chat_id, message="This is a specific chat!")

"""
[{
    _id: ObjectID(''),
    name: string, # Name of Chat
    messages: 
    'uuid': {
        parentId: null,
        childID: [],
        input: {
            message: string,
            timeStamp: 
        }
        output: {
            response: string
        }
    },
    'uuid': {
        parentId: null,
        childID: [],
        input: {
            message: string,
            timeStamp: 
        }
        output: {
            response: string
        }
    },

}]


example:

[{
    _id: ObjectID('hgjhvgb,kj'),
    name: 'Flask application', # Name of Chat
    messages: 
    'uuid': {
        parentId: null,
        childID: [],
        input: {
            message: string,
            timeStamp: 
        }
        output: {
            response: string
        }
    },
    'uuid': {
        parentId: null,
        childID: [],
        input: {
            message: string,
            timeStamp: 
        }
        output: {
            response: string
        }
    },

}]

"""
