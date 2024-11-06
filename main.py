from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import logging

from config.database import Database, DATABASE_URI
from controllers.adn_controller import DnaController
from controllers.mutant_controller import MutantController
from controllers.normal_controller import NormalController
from services.adn_validator_service import DnaTester
from schemas.adn_schema import DnaSchema

db = SQLAlchemy()

def create_flask_app():
    flask_app = Flask(__name__)

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("app.log"),  # Guardar logs en 'app.log'
            logging.StreamHandler()            # También mostrar logs en la consola
        ]
    )
    logger = logging.getLogger(__name__)

    flask_app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    db.init_app(flask_app)

    dna_controller = DnaController()
    dna_service = DnaTester()

    @flask_app.route("/mutant/", methods=["POST"])
    def check_mutant():
        dna_schema = DnaSchema(**request.get_json())
        dna = dna_schema.dna
        logger.info(f"Dna recibido: {dna}")
        if dna_service.isMutant(dna):
            logger.info(f"Es mutante")
            dna_type = "mutant"
            dna_controller.save_dna(dna=dna, dna_type=dna_type)
            return jsonify({"mutant":True})
        else:
            logger.info(f"Es un Humano normal")
            dna_type = "normal"
            dna_controller.save_dna(dna=dna, dna_type=dna_type)
            return jsonify({"mutant":False}), 403

    mutant_controller = MutantController()
    normal_controller = NormalController()

    @flask_app.route('/stats')
    def stats():
        count_mutant_dna = len(mutant_controller.get_all())
        count_human_dna = len(normal_controller.get_all())
        ratio = count_mutant_dna / (count_human_dna + count_mutant_dna)

        return jsonify({
            "count_mutant_dna": count_mutant_dna,
            "count_human_dna": count_human_dna,
            "ratio": ratio
        })

    @flask_app.route("/health_check/")
    def health_check():
        return "OK"

    return flask_app

def run_app(flask_app: Flask):
    flask_app.run(host="0.0.0.0", port=8000)

app = create_flask_app()
