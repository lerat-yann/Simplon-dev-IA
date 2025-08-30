-- a) Chiffre d’affaires total
SELECT SUM(prix * qte) AS chiffre_affaires_total
FROM ventes;

-- b) Ventes par produit
SELECT produit, SUM(prix * qte) AS ventes_par_produit
FROM ventes
GROUP BY produit
ORDER BY ventes_par_produit DESC;

-- c) Ventes par région
SELECT region, SUM(prix * qte) AS ventes_par_region
FROM ventes
GROUP BY region
ORDER BY ventes_par_region DESC;
