from flask import Blueprint, request, jsonify
from services.uni_services import UniService
from config.conexion import get_db_session
from flask_jwt_extended import create_access_token, jwt_required

uni_bp = Blueprint('uni', __name__)

service = UniService(get_db_session())


@uni_bp.route('/uni', methods=['GET'])
@jwt_required()
def get_universidades():
    universidades = service.listar_uni()
    return jsonify([{'id': u.id, 'nombre': u.nombre, 'codigo': u.codigo, 'carrera':u.carrera} for u in universidades]), 200

@uni_bp.route('/uni/<int:uni_id>', methods=['GET'])
def get_universidad(uni_id):
    uni = service.obtener_uni(uni_id)
    if uni:
        return jsonify({'id': uni.id, 'nombre': uni.nombre, 'codigo': uni.codigo, 'carrera':uni.carrera}), 200
    return jsonify({'error': 'Universidad no encontrada'}), 404

@uni_bp.route('/uni', methods=['POST'])
def create_universidad():
    data = request.get_json()
    nombre = data.get('nombre')
    carrera = data.get('carrera')
    codigo = data.get('codigo')
    if not nombre or not codigo:
        return jsonify({'error': 'Todos los campos son obligatorios'}), 400
    uni = service.crear_uni(nombre, codigo, carrera)
    return jsonify({'id': uni.id, 'nombre': uni.nombre, 'codigo': uni.codigo, 'carrera':uni.carrera}), 201

@uni_bp.route('/uni/<int:uni_id>', methods=['PUT'])
def update_universidad(uni_id):
    data = request.get_json()
    nombre = data.get('nombre')
    codigo = data.get('codigo')
    carrera = data.get('carrera')
    uni = service.actualizar_uni(uni_id, nombre, codigo, carrera)
    if uni:
        return jsonify({'id': uni.id, 'nombre': uni.nombre, 'codigo': uni.codigo,'carrera':uni.carrera}), 200
    return jsonify({'error': 'Cita de inscripcion no encontrada'}), 404

@uni_bp.route('/uni/<int:uni_id>', methods=['DELETE'])
def delete_universidad(uni_id):
    uni = service.eliminar_uni(uni_id)
    if uni:
        return jsonify({'message': 'Mataeria Eliminada'}), 200
    return jsonify({'error': 'Cita de inscripcion no encontrada'}), 404



