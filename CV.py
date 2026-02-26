
import streamlit as st
st.markdown("""
<style>
    .stApp {
        font-family: 'Times New Roman', Times, serif;
    }
    h1, h2, h3, p, li {
        font-family: 'Times New Roman', Times, serif !important;
    }
</style>
""", unsafe_allow_html=True)
st.sidebar.image("ME.jpg", width=200,)

# SIDEBAR - Infos personnelles 
st.sidebar.title("👩‍🔬 Aïssatou DIAGNE")
st.sidebar.markdown("""
📍 Née le 22 Juillet 2000 à Thiès  

✉️ aissatoumbene2000@gmail.com 

❤️ Célibataire sans enfant

🆔 Sénégalaise  

🌐 LANGUES  

• Wolof : Langue maternelle ⭐ 

• Français : Bonnes connaissances 

• Anglais : Connaissances de base  

🎯 LOISIRS

• Sport   

• Cuisine  


---
Merci pour votre temps & attention !

---
""")



st.title("AISSATOU DIAGNE")
st.markdown("**Géographe / Géomaticienne**")       

st.header("Profil")
st.write("Etudiante en BTS2 en Géomatique au CEDT le G15 à Dakar. Passionnée par les systèmes d’information géographique (SIG), l’analyse spatiale et la cartographie. Motivée à développer des compétences pratiques en géomatique et traitement de données spatiales.")
    
st.markdown("---")


st.header("FORMATIONS")
    

st.markdown("""
    **2025-2026**: BTS 2 en géomatique (en cours)  
    au Centre d'Entreprenariat et de Développement technique (CEDT LE G15)
    """)
    
st.markdown("""
    **2024-2025**: BTS 1 en géomatique  
    au Centre d'Entreprenariat et de Développement technique (CEDT LE G15)
    """)
    
st.markdown("""
    **2023-2024**: Master 2 (en cours) spécialisation hydrologie  
    au département de géographie à l'Université Cheikh Anta Diop de Dakar (UCAD)
    """)
    
st.markdown("""
    **2022-2023**: Master 1 en hydrologie  
    au département de géographie à l'Université Cheikh Anta Diop de Dakar (UCAD)
    """)
    
st.markdown("""
    **2021-2022**: Licence 3 en géographie  
    au département de géographie à l'Université Cheikh Anta Diop de Dakar (UCAD)
    """)
    
st.markdown("""
    **2020-2021**: Licence 2 en géographie  
    au département de géographie à l'Université Cheikh Anta Diop de Dakar (UCAD)
    """)
    
st.markdown("""
    **2019-2020**: Licence 1 en géographie  
    au département de géographie à l'Université Cheikh Anta Diop de Dakar (UCAD)
    """)
    
st.markdown("""
    **2018-2019**: Baccalauréat en série L2  
    au lycée Ahmadou Ndack Seck de Thiès (LANS)
    """)
st.markdown("---")

st.subheader("Attestations et Diplômes Complémentaires")

st.markdown("""

**Diplôme d'Honneur reçu lors de la Journée d'Excellence organisé par** la Table de concertation des chefs d'établissement de la formation professionnelle de Dakar:
*30/12/2025*

**Attestation de fin de stage**  
à la Direction Générale Surveillance et Contrôle Occupation du Sol (DGSCOS)
17/07 au 17/10/2025


**Attestation de réussite Licence en Géographie**  
à l'Université Cheikh Anta Diop de Dakar (UCAD):
08/05/2023


**Attestation de fin de formation en Informatique**  
Windows • Word • Excel • PowerPoint • Internet  
**Centre "Digital Unify" Espace Jeunes Thiès**:
21/09/2023
""")







 



st.header("COMPÉTENCES TECHNIQUES")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **SIG et Cartographie**  
    Maîtrise de QGIS/ArcGIS pour analyses spatiales, 
    création de cartes thématiques et traitement de données raster.
    Numérisation et Géoréférencement.
    
    **Télédétection**  
    Interprétation d'images satellitaires/drones, traitement GNSS 
    et levés topographiques.
    
    **Photogrammétrie**  
    Traitements d'images issues de drones pour modélisation 3D, 
    orthophotographie et reconstitution topographique.
    """)

with col2:
    st.markdown("""
    **Programmation**  
    Python (JupyterLab/Streamlit), webmapping (CSS/HTML), bases SQL.
    
    **Hydrologie**  
    délimitation de bassins versants, Initiation à la modélisation hydrologique  (Master UCAD).
    
    **Surveillance Foncière**  
    Application règles urbanisme, gestion PV/convocations (DGSCOS).
    """)

st.markdown("---")
st.header("COMPÉTENCES OPERATIONNELLES")
st.markdown("""
**Gestion Administrative** : Dossiers sensibles (plaintes, convocations, rapports de mission).

**Travaux Terrain** : Patrouilles surveillance foncière, détection infractions.

**Digitalisation** : Saisie Word, retranscription d'auditions, fiches mission.
""")

st.markdown("---")
st.header("EXPÉRIENCES PROFESSIONNELLES")
 
st.markdown("""
**STAGIAIRE** à la Direction Générale de la Surveillance et du Contrôle de l'Occupation du Sol

**• Patrouilles de terrain** pour la surveillance foncière et la détection d'infractions 
(occupations irrégulières, constructions non autorisées)

**• Interventions directes** : remise de convocations, arrêt de travaux illégaux, 
établissement et transmission de procès-verbaux

**• Rédaction, remplissage et gestion** de fiches de mission à remettre à la direction 
ou au secrétariat

**• Participation à la digitalisation** et à la saisie sous Word (retranscription 
d'auditions, rédaction de rapports)
""")
st.markdown("""
**• Numérisation et gestion de bases de données SIG** : Import de fichiers AutoCAD 
(DXF/DWG) dans ArcGIS, vectorisation des parcelles, création et mise à jour de bases 
de données attributaires, export vers formats KMZ et Excel (table attributaire).

**• Flux de travail complet** : Prise en charge fichiers CAO → géoréférencement → 
numérisation → enrichissement bases de données → exports interopérables (SHP→KMZ, 
attributs→Excel).
""")

st.markdown("---")
st.markdown("###  LOGICIELS UTILISÉS")
st.markdown("""
QGIS  
ArcGIS  
ERDAS  
Agisoft Metashape
Anaconda   
Google Earth  
PostgreSQL   
MicroStation  
AutoCAD  
Suite Bureautique
Anaconda
Pix4DMapper
""")
        
    







