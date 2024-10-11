from flask import jsonify, request, Blueprint
from bson.objectid import ObjectId
from marshmallow import Schema, fields, ValidationError
from src.config.db_config import employees_collection

db_crud = Blueprint('db_crud', __name__)

# Schema for Name field (first_name, middle_name, last_name)
class NameSchema(Schema):
    first_name = fields.Str(required=True)
    middle_name = fields.Str(missing=None)
    last_name = fields.Str(required=True)

# Schema for Address field (street, city, state, zip code)
class AddressSchema(Schema):
    street = fields.Str(required=True)
    city = fields.Str(required=True)
    state = fields.Str(required=True)
    zip_code = fields.Str(required=True)

# Main Employee Schema with nested fields
class EmployeeSchema(Schema):
    name = fields.Nested(NameSchema, required=True)
    address = fields.Nested(AddressSchema, required=True)
    email = fields.Email(required=True)
    phone = fields.Str(required=True)
    department = fields.Str(required=True)
    position = fields.Str(required=True)
    salary = fields.Float(required=True)

employee_schema = EmployeeSchema()
employee_list_schema = EmployeeSchema(many=True)

# Function to validate ObjectId
def is_valid_objectid(id):
    try:
        return ObjectId(id)
    except:
        return None

# 1. Get All Employees
@db_crud.route("/employees", methods=["GET"])
def get_all_employees():
    employees = list(employees_collection.find())
    for employee in employees:
        employee["_id"] = str(employee["_id"])
    return jsonify({"employees": employees}), 200

#2. create a new employee
@db_crud.route("/employees", methods=["POST"])
def create_employee():
    try:
        data = request.json        
        validated_result = employee_schema.load(data)
        # Insert the validated employee data into MongoDB
        query_result = employees_collection.insert_one(validated_result)
        # Get the inserted employee's ID
        inserted_id = str(query_result.inserted_id)  # Convert ObjectId to string
        # Optionally, if you don't want to return the _id:
        response_data = validated_result  # Copy validated data
        response_data['_id'] = inserted_id  # Include the inserted ID in the response if needed
        return jsonify({"message": "Employee created successfully", "data": request.json}), 201
        
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400


# 3. Get Employee Details by ID
@db_crud.route("/employees/<id>", methods=["GET"])
def get_employee_by_id(id):
    employee_id = is_valid_objectid(id)
    if not employee_id:
        return jsonify({"error": "Invalid ID"}), 400

    employee = employees_collection.find_one({"_id": employee_id})
    if employee:
        employee["_id"] = str(employee["_id"])
        return jsonify({"employee": employee}), 200
    return jsonify({"error": "Employee not found"}), 404

# 4. Update Employee Details by ID
@db_crud.route("/employees/<id>", methods=["PUT"])
def update_employee_by_id(id):
    employee_id = is_valid_objectid(id)
    if not employee_id:
        return jsonify({"error": "Invalid ID"}), 400

    try:
        data = request.json
        employee_schema.load(data)  # Validate schema
        result = employees_collection.update_one({"_id": employee_id}, {"$set": data})

        if result.modified_count > 0:
            return jsonify({"message": "Employee updated successfully"}), 200
        else:
            return jsonify({"error": "No changes made"}), 404
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

# 5. Delete Employee Details by ID
@db_crud.route("/employees/<id>", methods=["DELETE"])
def delete_employee_by_id(id):
    employee_id = is_valid_objectid(id)
    if not employee_id:
        return jsonify({"error": "Invalid ID"}), 400

    result = employees_collection.delete_one({"_id": employee_id})

    if result.deleted_count > 0:
        return jsonify({"message": "Employee deleted successfully"}), 200
    return jsonify({"error": "Employee not found"}), 404
