import React, { useState, useEffect } from "react";
import "./App.css"; // On ajoute ce fichier CSS

function App() {
  const [terrasses, setTerrasses] = useState([]);
  const [filter, setFilter] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchData = async (arrondissement = "") => {
    setLoading(true);
    setError(null);
    let url = "http://localhost:5000/api/data";
    if (arrondissement) {
      url += `/arrondissement?value=${arrondissement}`;
    }

    try {
      const res = await fetch(url);
      if (!res.ok) throw new Error("Erreur lors de la récupération");
      const data = await res.json();
      setTerrasses(data);
    } catch (err) {
      setError(err.message);
    }
    setLoading(false);
  };

  useEffect(() => {
    fetchData();
  }, []);

  const handleFilterChange = (e) => {
    const val = e.target.value;
    setFilter(val);
    fetchData(val);
  };

  return (
    <div className="container">
      <h1>Terrasses autorisées à Paris</h1>

      <label htmlFor="filterInput" className="filter-label">
        Filtrer par arrondissement :
      </label>
      <input
        id="filterInput"
        type="text"
        value={filter}
        onChange={handleFilterChange}
        placeholder="Ex: 75001"
        className="filter-input"
      />

      {loading && <p className="loading">Chargement...</p>}
      {error && <p className="error">Erreur : {error}</p>}

      <div className="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Nom Enseigne</th>
              <th>Adresse</th>
              <th>Arrondissement</th>
              <th>Typologie</th>
              <th>Longueur</th>
              <th>Largeur</th>
              <th>Affichette</th>
            </tr>
          </thead>
          <tbody>
            {terrasses.length === 0 && !loading && (
              <tr>
                <td colSpan="7" className="no-data">
                  Aucune donnée
                </td>
              </tr>
            )}
            {terrasses.map((t) => (
              <tr key={t.id}>
                <td>{t.nom_enseigne}</td>
                <td>{t.adresse}</td>
                <td>{t.arrondissement}</td>
                <td>{t.typologie}</td>
                <td>{t.longueur}</td>
                <td>{t.largeur}</td>
                <td>
                  {t.lien_affichette ? (
                    <a href={t.lien_affichette} target="_blank" rel="noreferrer">
                      Voir
                    </a>
                  ) : (
                    "N/A"
                  )}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default App;
