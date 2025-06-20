from flask import Flask, jsonify, request
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Terrasse
from scraper import fetch_terrasses

app = Flask(__name__)
CORS(app)

DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "root")
DB_HOST = os.getenv("DB_HOST", "db") 
DB_NAME = os.getenv("DB_NAME", "terrasses_db")

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)

@app.route("/api/data", methods=["GET"])
def get_all_data():
    session = Session()
    terrasses = session.query(Terrasse).all()
    session.close()

    # Convertir en dicts JSON serializables
    result = []
    for t in terrasses:
        result.append({
            "id": t.id,
            "typologie": t.typologie,
            "adresse": t.adresse,
            "arrondissement": t.arrondissement,
            "nom_enseigne": t.nom_enseigne,
            "longueur": t.longueur,
            "largeur": t.largeur,
            "lien_affichette": t.lien_affichette
        })
    return jsonify(result)


@app.route("/api/data/<string:filtre>", methods=["GET"])
def get_data_filtered(filtre):

    champ = filtre
    valeur = request.args.get("value")
    if not valeur:
        return jsonify({"error": "Paramètre 'value' manquant"}), 400

    # Liste des champs autorisés à filtrer (sécurité)
    champs_autorises = {"arrondissement", "typologie", "nom_enseigne", "adresse"}
    if champ not in champs_autorises:
        return jsonify({"error": "Filtre non autorisé"}), 400

    session = Session()
    filt = {champ: valeur}
    terrasses = session.query(Terrasse).filter_by(**filt).all()
    session.close()

    result = []
    for t in terrasses:
        result.append({
            "id": t.id,
            "typologie": t.typologie,
            "adresse": t.adresse,
            "arrondissement": t.arrondissement,
            "nom_enseigne": t.nom_enseigne,
            "longueur": t.longueur,
            "largeur": t.largeur,
            "lien_affichette": t.lien_affichette
        })
    return jsonify(result)


@app.route("/api/scrape", methods=["POST"])
def trigger_scrape():
    try:
        session = Session()
        terrasses = fetch_terrasses(limit=50)
        session.bulk_save_objects(terrasses)
        session.commit()
        session.close()
        return jsonify({"message": f"{len(terrasses)} enregistrements insérés"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Endpoint non trouvé"}), 404

@app.errorhandler(500)
def internal_error(e):
    return jsonify({"error": "Erreur serveur interne"}), 500


if __name__ == "__main__":
    app.run(debug=True)
