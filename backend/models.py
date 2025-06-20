from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Terrasse(Base):
    __tablename__ = "terrasses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    typologie = Column(String(255))
    adresse = Column(String(255))
    arrondissement = Column(String(50))
    nom_enseigne = Column(String(255))
    longueur = Column(Float)
    largeur = Column(Float)
    lien_affichette = Column(String(1024))
