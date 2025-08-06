from flask import Blueprint, jsonify

from configuration.logging_configuration import logger as log

actuator_bp = Blueprint('actuator', __name__, url_prefix='/py-fea/actuator')


@actuator_bp.route('/health', methods=['GET'])
def health():
    log.debug("[INCOMING REQUEST] - Health actuator")
    return jsonify(status="healthy"), 200


@actuator_bp.route('/readiness', methods=['GET'])
def readiness():
    log.debug("[INCOMING REQUEST] - Ready actuator")
    return jsonify(status="ready"), 200
