import requests
from models import Terrasse

def fetch_terrasses(limit=100):
    url = "https://opendata.paris.fr/api/records/1.0/search/"
    params = {
        "dataset": "terrasses-autorisations",
        "rows": limit
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    results = []
    for record in data.get("records", []):
        fields = record.get("fields", {})

        # Créer une instance Terrasse, PAS un dict
        terrasse = Terrasse(
            typologie=fields.get("typologie"),
            adresse=fields.get("adresse"),
            arrondissement=fields.get("arrondissement"),
            nom_enseigne=fields.get("nom_enseigne"),
            longueur=fields.get("longueur"),
            largeur=fields.get("largeur"),
            lien_affichette=fields.get("lien_affichette")
        )

        results.append(terrasse)

    return results
