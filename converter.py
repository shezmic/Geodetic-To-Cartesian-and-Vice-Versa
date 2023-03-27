/**
 * @author [shezmic]
 * @email [mcwambua@gmail.com]
 * @create date 2019-03-05 02:39:08
 * @modify date 2023-03-27 09:34:08
 * @desc [description]
 */

    
import pyproj

# Function to convert Cartesian coordinates to Geodetic
def cartesian_to_geodetic(x, y, z):
    # Define the coordinate systems
    ecef = pyproj.Proj(proj='geocent', ellps='WGS84', datum='WGS84')
    lla = pyproj.Proj(proj='latlong', ellps='WGS84', datum='WGS84')
    # Perform the coordinate transformation
    lon, lat, alt = pyproj.transform(ecef, lla, x, y, z, radians=False)
    return lat, lon, alt

# Function to convert Geodetic coordinates to Cartesian
def geodetic_to_cartesian(lat, lon, alt):
    # Define the coordinate systems
    ecef = pyproj.Proj(proj='geocent', ellps='WGS84', datum='WGS84')
    lla = pyproj.Proj(proj='latlong', ellps='WGS84', datum='WGS84')
    # Perform the coordinate transformation
    x, y, z = pyproj.transform(lla, ecef, lon, lat, alt, radians=False)
    return x, y, z

def main():
    # Get user's choice of conversion
    choice = input("Enter A (Cartesian to Geodetic) or B (Geodetic to Cartesian)\n")

    if choice == 'A':
        # Get Cartesian coordinates from user
        x = float(input("Enter X coordinate: "))
        y = float(input("Enter Y coordinate: "))
        z = float(input("Enter Z coordinate: "))
        # Perform conversion and display results
        lat, lon, alt = cartesian_to_geodetic(x, y, z)
        print(f"\nLatitude: {lat}\nLongitude: {lon}\nHeight in metres: {alt}")

    elif choice == 'B':
        # Get Geodetic coordinates from user
        lat = float(input("Enter Latitude: "))
        lon = float(input("Enter Longitude: "))
        alt = float(input("Enter Height in metres: "))
        # Perform conversion and display results
        x, y, z = geodetic_to_cartesian(lat, lon, alt)
        print(f"\nX: {x}\nY: {y}\nZ: {z}")

    else:
        print("Sorry, wrong selection...")
        return

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
