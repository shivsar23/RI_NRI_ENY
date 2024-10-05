import numpy as np

Giri = [(17.5,91.5),(17.5,91.5),(17.5,91.5),(17.5,91.5),(17.5,91.5),(17.5,91.5),(17.5,91.5),(17.5,91.5),(18.0,92),(18.0,92),
 (18.0,92.0),(18.5,92.5),(18.5,92.5),(19.0,93),(19.0,93),(19.5,93.5),(19.8,93.5),(20.0,93.5),
 (20.5,94),(20.5,94),(21.0,94.5),(21.5,95),(22.0,95.5),]

Phailin = [(12.0,96.0),(12.0,95.5),(12.0,95),(12.0,94.5),(12.25,94.25),(12.5,94.0),(12.75,93.75), (13.0,93.5),(13.0,93.5),(13.0,93.0),(13.5,92.5),
 (13.5,92.5),(13.6,92.5),(14.0,92.0),(14.0,92.0),(14.5,91.5),(14.5,91.0),(15.0,90.5),(15.0,90.5),
 (15.5,90.0),(15.5,90.0),(15.5,89.5),(15.5,89.0),(16.0,88.5),(16.0,88.5),(16.2,88.3),(16.5,88.0),
 (16.8,87.7),(16.9,87.2),(17.0,87.0),(17.1,86.8),(17.5,86.5),(17.8,86.0),(18.1,85.7),(18.6,85.4),
 (18.7,85.2),(19.1,85.2),(19.5,84.8),(20.0,84.5),(20.5,84.5),(21.0,84.0),(21.5,84.0),(21.8,83.8),
 (22.5,83.8),(22.75,83.65),(23.0,83.5),(23.25,83.75),(23.5,84.0),(24.0,84.1),(24.5,84.2),]



Madi = [(10.0,84.0),(10.0,84.0),(10.1,84.0),(10.2,84.0),(10.3,84.0),(10.4,84.0),(10.45,84.05),(10.5,84.1),(10.5,84.1),(10.7,84.2),(10.8,84.3),
 (11.0,84.4),(11.0,84.5),(11.2,84.5),(11.5,84.6),(11.8,84.6),(12.0,84.6),(12.3,84.7),(12.6,84.7),
 (13.0,84.7),(13.2,84.7),(13.4,84.7),(13.6,84.7),(13.8,84.7),(14.0,84.7),(14.3,84.7),(14.4,84.7),
 (14.6,84.7),(14.7,84.7),(14.8,84.8),(14.8,84.8),(15.0,85.0),(15.3,85.3),(15.4,85.3),(15.7,85.3),
 (15.4,85.0),(15.1,84.8),(14.9,84.7),(14.6,84.6),(14.3,84.2),(14.0,83.8),(13.7,83.5),(13.5,83.4),
 (13.3,83.3),(13.1,83.5),(12.9,82.7),(12.7,82.35),(12.5,82.0),(12.0,81.5),(11.5,81.2),(11.0,80.7),(10.5,80.0),(10.25,78.9),(10.0,78.8),]



Hudhud=[(11.5, 95.0), (11.7, 94.8), (11.85,94.4),(12.0, 94.0), (12.0,93.75),(12.0, 93.5),(12.1,93.25), (12.2, 93.0), (12.3, 92.9), (12.5, 92.5), (12.7, 91.7),
 (12.8, 91.0), (13.0, 90.5), (13.2, 90.2), (13.5, 89.6), (13.7, 89.2), (13.8, 89.0), (13.9, 88.8), (14.6, 88.6),
 (14.1, 88.4), (14.1, 88.1), (14.1, 87.9), (14.3, 87.7), (14.4, 87.6), (14.7, 87.2), (14.8, 87.0), (15.0, 86.8),
 (15.2, 86.7), (15.4, 86.5), (15.5, 86.4), (15.7, 86.1), (15.9, 85.7), (16.0, 85.4), (16.1, 85.1), (16.1, 85.0),
 (16.2, 84.8), (16.2, 84.8), (16.4, 84.7), (16.7, 84.4), (17.2, 84.2), (17.4, 83.8), (17.6, 83.4), (17.8, 83.0),
 (18.0, 82.7), (18.3, 82.5), (18.7, 82.3), (18.7, 82.3), (19.5, 81.5), (20.5, 81.5), (20.7, 81.5),(21.0,81.5), (21.3, 81.5),(21.8,81.5),
 (22.3, 81.5),(23.55,81.5), (24.8, 81.5), (25.1, 81.6), (25.6, 81.7), (26.3, 81.8),]


Ockhi=[(6.5, 81.8), (6.5, 80.4), (6.2, 80.0), (6.3, 79.2), (6.5, 78.6), (6.7, 78.3), (7.5, 77.5), (7.8, 76.9),
 (7.9, 76.4), (8.2, 75.8), (8.3, 75.4), (8.5, 74.9), (8.6, 74.5), (8.8, 74.0), (8.9, 73.8), (9.0, 73.4),
 (9.1, 73.0), (9.2, 72.8), (9.3, 72.5), (9.4, 72.1), (9.5, 71.8), (9.6, 71.5), (9.7, 71.2), (9.8, 71.0),
 (10.2, 70.6), (10.5, 70.3), (10.8, 70.0), (11.1, 69.7), (11.3, 69.5), (11.7, 69.2), (12.1, 69.0), (12.3, 68.9),
 (12.4, 68.8), (12.9, 68.7), (13.1, 68.6), (13.5, 68.5), (14.0, 68.5), (14.5, 68.5), (14.7, 68.5), (14.9, 68.7),
 (15.2, 69.0), (15.7, 69.2), (16.1, 69.5), (16.5, 69.8), (16.9, 70.1), (17.3, 70.4), (17.7, 70.7), (18.1, 71.0),
 (18.3, 71.2), (18.5, 71.4), (18.8, 71.6), (19.2, 71.9),]


Titli=[(14.0, 88.8), (14.0, 88.8),(14.15,88.5), (14.3, 88.2),(14.4,87.9), (14.5, 87.6),(14.6,87.35), (14.7, 87.1), (14.7, 86.9), (14.8, 86.7), (14.9, 86.6),
 (15.1, 86.4), (15.3, 86.2), (15.5, 86.0), (15.7, 85.8), (16.0, 85.8), (16.5, 85.8), (17.0, 85.6), (17.3, 85.4),
 (17.5, 85.3), (17.7, 85.2), (18.2, 85.1), (18.6, 84.7), (18.8, 84.4), (19.0, 84.1), (19.3, 83.8), (19.6, 83.8), 
 (19.9, 83.7), (20.1, 84.0), (20.3, 84.3),(20.4,84.5), (20.5, 84.7), (20.6, 84.9), (20.8, 85.2), (20.9, 85.5), (21.2, 86.1), (21.55,86.65),
 (21.9, 87.2), (22.1, 87.5),]

Fani=[(2.7, 89.7),(2.7, 89.7), (3.0, 89.4), (3.1, 89.3), (3.2, 89.2), (3.45, 89), (3.7, 88.8), (4.1, 88.8), (4.5, 88.8),
 (4.9, 88.7), (5.2, 88.6), (5.4, 88.5), (5.9, 88.5),(6.3, 88.5), (6.6, 88.2), (6.9, 87.9), (7.3, 87.9), 
 (7.3, 87.9), (7.4, 87.8), (7.7, 87.5), (8.2, 87.0),(8.3, 86.9), (8.4, 86.9), (8.5, 86.9), (8.6, 86.9),
 (8.7, 86.9), (9.2, 86.9), (9.7, 86.8), (10.1, 86.7), (10.4, 86.7), (10.8, 86.6), (11.1, 86.5), (11.7, 86.5),
 (12.3, 86.2), (12.6, 85.7), (13.0, 85.3), (13.3, 84.7), (13.4, 84.5), (13.5, 84.4), (13.6, 84.2), (13.9, 84.0),
 (14.1, 83.9), (14.2, 83.9), (14.5, 84.1), (14.9, 84.1), (15.1, 84.1), (15.2, 84.1), (15.5, 84.2), (15.9, 84.5),
 (16.2, 84.6), (16.7, 84.8), (17.1, 84.8), (17.5, 84.8), (17.8, 84.9), (18.2, 85.0), (18.6, 85.2), (19.1, 85.5),
 (19.6, 85.7), (20.2, 85.9), (20.6, 86.0), (21.1, 86.5), (21.5, 86.7), (21.9, 87.1), (22.5, 87.9), (23.1, 88.2),
 (23.6,  88.8), (24.3, 89.3),(24.75,90.0), (25.2, 90.7),]


Bulbul=[(13.1, 91.5), (13.1, 91.0), (13.1, 90.7),(13.15,90.4), (13.2, 90.1),(13.25,89.95), (13.3, 89.8),(13.35,89.75), (13.4, 89.7), (13.4, 89.6), (13.4, 89.4),
 (13.45,89.35),(13.5, 89.3),(13.65,89.3), (13.8, 89.3),(14.0,89.3), (14.2, 89.3), (14.7, 89.3), (15.3, 88.7), (15.5, 88.4), (15.9, 88.0), (16.2, 87.9), 
 (16.4, 87.8), (16.6, 87.7), (16.9, 87.6), (17.2, 87.6), (17.6, 87.6), (18.1, 87.6), (18.5, 87.6), (19.2, 87.7), 
 (19.3, 87.6), (19.6, 87.7), (20.0, 87.6), (20.4, 87.6), (20.6, 87.8), (20.9, 87.9), (21.2, 88.1), (21.4, 88.3), 
 (21.6, 88.6), (21.9, 89.1), (22.1, 89.5), (22.2, 89.7), (22.3, 90.0), (22.4, 90.1), (22.5, 90.4),(22.6,90.8),(22.7, 91.2), (22.9,91.55),
 (23.1, 91.9),]


Amphan=[(10.4, 87.0), (10.7, 86.5), (10.9, 86.3), (10.9, 86.3), (10.9, 86.3), (11.0, 86.2), (11.1, 86.1), (11.3, 86.1), 
 (11.4, 86.0), (11.4, 86.0), (11.5, 86.0), (11.7, 86.0), (12.0, 86.0), (12.8, 86.2), (12.5, 86.1), (12.9, 86.4), 
 (13.2, 86.3), (13.3, 86.2), (13.4, 86.2), (13.7, 86.2), (14.0, 86.3), (14.5, 86.4), (14.9, 86.5), (15.2, 86.6), 
 (15.6, 86.7), (16.0, 86.8), (16.5, 86.9), (17.0, 86.9), (17.4, 87.0), (18.1, 87.1), (18.4, 87.2), (18.7, 87.2), 
 (19.1, 87.5), (19.8, 87.7), (20.6, 88.0), (21.4, 88.1), (21.9, 88.4), (22.7, 88.6), (23.3, 89.0), (24.2, 89.0), 
 (24.2, 89.3), (24.7, 89.5), (25.0, 89.6), (25.2,89.6), (25.4, 89.6),]


Mocha=[(8.3, 89.5),(8.4,89.4), (8.5, 89.3),(8.5,89.15), (8.5, 89.0), (8.8, 88.9), (9.1, 88.7),(9.55,88.55), (10.0, 88.4),(10.4,88.3), (10.8, 88.2),(11,88.15), (11.2, 88.1),
 (11.4, 88.0), (11.6, 88.0), (11.8, 88.0), (12.2, 88.0), (12.5, 88.1), (12.7, 88.1), (12.9, 88.1), (13.2, 88.1),
 (13.6, 88.2), (14.0, 88.3), (14.3, 88.4), (14.6, 88.6), (14.8, 88.7), (15.1, 88.8), (15.2, 88.9), (15.4, 89.1),
 (15.7, 89.5), (16.0, 90.0), (16.4, 90.3), (16.9, 90.8), (17.4, 90.9), (17.9, 91.0), (18.3, 91.3), (18.7, 91.5),
 (19.3, 91.9), (19.9, 92.5), (20.5, 92.9), (21.1, 93.3), (21.8, 93.8), (22.7, 94.6), (23.5, 95.3), (23.9, 97.8),]


Mala=[(9.5, 90.5), (9.5, 90.5), (9.5, 90.0), (10.0, 89.5), (10.0, 89.5), (10.0, 89.5), (10.0, 89.5), (10.5, 89.0), (10.5, 89.0),
 (11.0, 89.0), (11.0, 89.5), (11.5, 90.0), (12.0, 90.5), (12.0, 90.5), (12.0, 90.5), (12.0, 90.5), (12.5, 90.5), (12.5, 90.5),
 (12.5, 90.5), (13.0, 90.5), (13.0, 90.5), (13.0, 90.5), (13.5, 90.5), (14.0, 91.0), (14.5, 91.5), (15.0, 92.0), (15.3, 92.3), 
 (15.5, 92.5), (16.0, 93.0), (16.0, 93.0), (16.5, 93.5), (16.5, 93.5), (17.0, 94.0), (17.5, 94.5), (18.0, 95.0), (18.5, 95.5),
 (18.5, 95.5), (19.0, 96.0),]



Sidr=[(10.0, 92.0), (10.0, 92.0), (10.0, 92.0), (10.5, 91.5), (10.5, 91.5), (10.5, 91.5), (10.5, 91.0), (11.0, 90.5), (11.0, 90.5),
      (11.5, 90.0), (11.5, 90.0), (11.5, 90.0), (11.5, 90.0), (12.0, 89.5), (12.0, 89.5), (12.0, 89.5), (13.0, 89.5), (13.0, 89.5),
      (13.0, 89.5), (13.5, 89.5), (14.0, 89.5), (14.5, 89.5), (14.5, 89.5), (15.0, 89.5), (15.5, 89.5), (16.0, 89.0), (16.0, 89.0), 
      (16.5, 89.0), (17.0, 89.0), (17.5, 89.0), (18.0, 89.0), (19.5, 89.0), (20.0, 89.0), (21.0, 89.0), (21.5, 89.5), (22.5, 90.5), 
      (23.5, 91.0), (23.5, 91.0), (24.5, 91.5),]



Nargis=[(12.0, 87.0), (12.0, 87.0), (12.0, 86.5), (12.0, 86.5), (12.0, 86.5), (12.5, 86.0), (13.0, 85.5), (13.0, 85.5), (13.0, 85.5),
        (13.0, 85.5), (13.0, 85.5), (13.0, 85.5), (13.0, 85.5), (13.0, 85.5), (13.0, 85.5), (13.0, 85.5), (13.5, 85.5), (13.5, 85.5), 
        (13.5, 85.5), (14.0, 85.5), (14.0, 85.5), (14.0, 85.5), (14.0, 86.0), (14.0, 86.0), (14.5, 86.5), (14.5, 86.5), (14.5, 87.0), 
        (14.5, 87.0), (15.0, 87.5), (15.0, 87.5), (15.0, 87.5), (15.5, 88.0), (15.5, 89.0), (16.0, 89.5), (16.0, 90.0), (16.0, 90.5), 
        (16.0, 91.0), (16.0, 91.5), (16.0, 92.0), (16.0, 92.5), (16.0, 93.0), (16.0, 93.5), (16.0, 94.0), (16.0, 94.3), (16.0, 95.0), 
        (16.5, 95.5), (16.5, 95.5), (16.5, 95.5), (17.0, 96.0), (17.5, 96.5), (18.0, 97.0),]

dc = {}

dc["giri"]=Giri
dc["phailin"]=Phailin
dc["madi"]=Madi
dc["hudhud"]=Hudhud
dc["ockhi"]=Ockhi
dc["titli"]=Titli
dc["fani"]=Fani
dc["bulbul"]=Bulbul
dc["amphan"]=Amphan
dc["mocha"]=Mocha
dc["mala"]=Mala
dc["sidr"]=Sidr
dc["nargis"]=Nargis

np.save("/DISK-0/gokul/ENGY/track.npy",dc) 