/**
 * @author [shezmic]
 * @email [mcwambua@gmail.com]
 * @create date 2019-03-05 02:39:08
 * @modify date 2019-03-05 02:39:08
 * @desc [description]
 */

import pyproj

# Definition of the function to convert Cartesian coordinates to Geodetic
def cartesian_to_geodetic(x, y, z):
    ecef = pyproj.Proj(proj='geocent', ellps='WGS84', datum='WGS84')
    lla = pyproj.Proj(proj='latlong', ellps='WGS84', datum='WGS84')

    lon, lat, alt = pyproj.transform(ecef, lla, x, y, z, radians=False)

    print("\n")
    print ("Latitude: %f" % lat)
    print ("Longitude: %f" % lon)
    print ("Height in metres: %f" % alt)


# Definition of the function to convert Geodetic coordinates to Cartesian
def geodetic_to_cartesian(lat, lon, alt):
    ecef = pyproj.Proj(proj='geocent', ellps='WGS84', datum='WGS84')
    lla = pyproj.Proj(proj='latlong', ellps='WGS84', datum='WGS84')

    x, y, z = pyproj.transform(lla, ecef, lon, lat, alt, radians=False)

    print("\n")
    print ("X: %f" % x)
    print ("Y: %f" % y)
    print ("Z: %f" % z)

# Brings up a prompt, basically just to make it easier for the user to enter the values
choice = input("Enter A (Cartesian to Geodetic) or B (Geodetic to Cartesian)" + "\r\n")

# Self explanatory
if choice == 'A':
    print("You chose Cartesian to Geodetic." + "\r\n")
    print("Enter these values: " + "\n")
    x = input("Enter X coordinate:  ")
    y = input("Enter Y coordinate:  ")
    z = input("Enter Z coordinate:  ")
    cartesian_to_geodetic(x, y, z)

# Self Explanatory too
elif choice == 'B':
    print("You chose Geodetic to Cartesian." + "\r\n")
    print("Enter these values: " + "\n")
    lat = input("Enter Latitude:  ")
    lon = input("Enter Longitude:  ")
    alt = input("Enter Height in metres:  ")
    geodetic_to_cartesian(lat, lon, alt)

# Unless someone is trying to play chess or something else other than do their homework ...lol
else:
    print("Sorry wrong selection...")
    exit
