import os
from math import cos, sin, radians
import matplotlib.pyplot as plt
from adafruit_rplidar import RPLidar
import numpy as np
import time
#.............................................................................
#gestion du mapping

nb_ligne_matrice=10000
nb_colonne_matrice=10000
matrice_stockage=np.zeros((nb_ligne_matrice,nb_colonne_matrice))

x_translation=0
y_translation=0

#.............................................................................
# Create a figure and axis for the plot
fig, ax = plt.subplots()

# used to scale data to fit on the screen
max_distance = 10000

#gestion des données du lidar
def process_data(data,translationx,translationy):

    ax.clear()  # Clear the previous plot
    ax.set_xlim(-max_distance, max_distance)
    ax.set_ylim(-max_distance, max_distance)
    ax.set_aspect('equal', adjustable='box')  # Set aspect ratio to equal for correct scaling

    #on recupere la matrice du lidar
    for angle, distance in enumerate(data):
        if distance != -1:
            # Convert polar coordinates to Cartesian coordinates
            x = distance * cos(radians(angle))+x_translation
            y = distance * sin(radians(angle))+y_translation

            #gestion de la position du robot pour le lidar
            # x=x+x_translation
            # y=y+y_translation

            #................................................................
            #stockage des retours lidar dans la matrice matrice_stockage
            matrice_stockage[round(x)+5000+x_translation][round(y)+5000+y_translation]=1
            #................................................................
            plt.xlabel('<- arrière du robot            &            avant du robot ->')
            plt.ylabel('Plan détection LIDAR')
            ax.plot(x, y, 'bo', markersize=1)  # Plot each point

            #affichage de la matrice de stockage
            #print("la matrice de stockage est ",matrice_stockage)
            #np.savetxt('matrice.txt', matrice_stockage, delimiter=' ', fmt='%d')
            #print("salut")


    plt.draw()
    plt.pause(3)
    print("Fin du graphique")
    #plt.close()

    #plt.clf()

    #print("salut les filles")
    #np.savetxt('matrice.txt', matrice_stockage, delimiter=' ', fmt='%d')
    #plt.pause(100)

try:
    # for scan in lidar.iter_scans():
    #     scan_data = [-1.0] * 360  # Initialize data for each new scan
    #     for (_, angle, distance) in scan:
    #         ang = int(angle) % 360
    #         scan_data[ang] = distance
    #on définit scan_data
    scan_data=[940.5, 933.0, 932.25, 925.0, 924.25, 918.75, 917.75, 913.75, 909.75, 909.75, 908.25, 905.0, 902.75, 902.5, 901.25, 900.5, 900.5, 901.0, 900.0, 899.75, 900.75, 902.75, 906.0, 906.5, 907.25, 910.75, 912.5, 913.25, 919.5, 924.0, 924.0, 928.0, 932.5, 937.5, 942.0, 949.0, 949.25, 957.5, 966.5, 977.0, 977.75, 986.25, 997.0, 1001.5, 1009.75, 1024.5, 1037.75, 1042.5, 1052.0, 1067.25, 1073.25, 1087.25, 1101.25, 1125.75, 1130.5, 1146.75, 1168.25, 1179.75, 1188.5, 1217.5, 1245.75, 1256.0, 1276.25, 1307.25, 1318.75, 1340.0, 1378.25, 1423.5, 1434.75, 1463.25, 1514.0, 1563.75, 1583.75, 1625.5, 1686.25, 1706.25, 1783.5, 1823.75, 1903.25, 1946.25, 1999.25, 2101.0, 2223.25, 2277.25, 2340.5, 2435.5, 2444.75, 2434.75, 2411.25, 2387.0, 2387.0, 2420.5, 2632.75, 3603.25, 3604.0, 3614.75, 3565.0, 2480.5, 2464.0, 2407.5, 2387.0, 2364.25, 2349.0, 2341.75, 2346.75, 2369.5, 2415.25, 2420.0, 3211.0, 3213.25, 3219.0, 3220.5, 3184.5, 3632.0, 3672.25, 3695.25, 3292.25, 3376.5, 3353.5, 3418.25, 2444.75, 2521.5, 2452.25, 2524.5, 2556.5, 2404.25, 2726.0, 2888.0, 2693.0, 2650.75, 2618.5, 2611.75, 2605.75, 2630.25, 2642.0, 2683.75, 2716.0, 2767.5, 1740.5, 1736.5, 1567.75, 1521.0, 1432.75, 1582.75, 1666.5, 1692.5, 1708.75, 1704.0, 1706.0, 1703.25, 1702.75, 1671.5, 5077.75, 5124.5, 5137.0, 5114.5, 1655.5, 5122.0, 8149.75, 9108.0, 9147.75, 9054.0, 9016.5, 9096.75, 8799.0, 7598.25, 7391.75, 7463.75, 7278.5, 5339.75, 5218.0, 8001.5, 6610.25, 6604.0, 6482.25, 6416.75, 6416.0, 6430.75, 6616.5, 7681.0, 6388.0, 6554.75, 6687.75, 5869.0, 4741.25, 6407.5, 6482.25, 6400.5, 6391.75, 6494.25, 6352.25, 6355.25, 6438.75, 6975.25, 6442.5, 6378.25, 7253.25, 7283.5, 7040.25, 685.75, 6244.25, 7026.25, 6364.75, 6326.75, 6233.25, 6518.25, 169.5, 6324.0, 6462.25, 6303.25, 6407.5, 5460.0, 6700.5, 5419.25, 5411.5, 5362.0, 5364.25, 5296.75, 6604.0, 6584.25, 6620.5, 6520.25, 6546.5, 6620.5, 6704.75, 5192.5, 8093.5, 6830.75, 6857.25, 7313.75, 7026.25, 7068.75, 6649.75, 6804.25, 7155.0, 5195.0, 6739.0, 134.25, 6704.75, 5200.0, 6679.25, 6662.25, 5249.25, 5510.0, 5283.5, 137.0, 5571.25, 136.25, 5361.5, 136.5, 136.5, 136.75, 234.25, 136.5, 145.0, 136.5, 136.5, 145.5, 136.25, 145.5, 138.25, 494.0, 140.75, 137.75, 141.0, 476.25, 138.0, 499.5, 137.75, 138.25, 138.25, 138.0, 138.5, 138.5, 142.0, 138.5, 139.25, 141.0, 141.0, 5386.0, 5703.75, 5164.5, 5137.0, 5286.25, 8272.75, 8570.0, 8951.75, 8672.25, 5513.0, 5307.5, 5521.5, 5703.75, 5530.25, 6185.75, 6142.5, 5427.75, 5063.25, 4888.0, 4327.0, 3923.5, 3734.25, 3566.25, 3453.25, 3286.25, 2998.75, 2897.25, 2738.5, 2555.25, 1748.5, 1698.0, 1593.0, 1551.0, 1510.25, 1461.5, 1467.5, 1477.0, 1491.75, 1505.25, 1515.0, 1535.25, 1557.0, 1557.0, 1550.25, 1496.5, 1460.25, 1433.75, 1399.75, 1571.75, 1516.25, 1464.75, 1326.5, 1305.25, 1304.75, 1264.75, 1254.75, 1241.5, 1206.75, 1182.0, 1169.5, 1138.25, 1118.0, 1107.0, 1092.0, 1080.25, 1070.0, 1059.5, 1044.75, 1038.75, 1030.5, 1015.5, 1008.5, 1007.5, 992.0, 989.25, 976.5, 962.5, 962.0, 954.5, 949.0, 944.5]
    #while(1):
    #plt.subplots()
    process_data(scan_data,x_translation,y_translation)

    #plt.close()
    x_translation=300
    y_translation=500
    #time.sleep(3000)
    process_data(scan_data,x_translation,y_translation)

    #affichage de la matrice
    #np.savetxt('matrice.txt', matrice_stockage, delimiter=' ', fmt='%d')

    #affichage_mapping()
    #print("affichage 1 fait")

    # for i in range(len(scan_data)):
    #     scan_data[i]+=200
    #     print("Salut")
           

    #print(type(scan_data[0]))

except KeyboardInterrupt:
    print('Stopping.')