import requests
import json
import os

def recognize_plate(filename):
    path=os.path.dirname(os.path.abspath(__file__))

    image_path= os.path.join(path,'saved_img',filename)
    # Set your API key and endpoint URL
    API_KEY = 'a8dfed6caef265edce7da0bd97c8bf3b040ef463'
    API_URL = 'https://api.platerecognizer.com/v1/plate-reader/'

    # Read the image file as binary data
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()

    # Construct the data payload
    data = {'regions': 'in'}

    # Make the API request
    response = requests.post(API_URL,
                             data=data,
                             headers={'Authorization': f'Token {API_KEY}'},
                             files={'upload': image_data})

    try:
        # Parse the JSON response
        results = json.loads(response.text)

        # Extract license plate information if available
        if 'results' in results:
            plate_info = results['results'][0]
            plate = plate_info['plate']
            confidence = plate_info['score']
            #return f'License plate: {plate} (confidence {confidence})'
            return plate

        else:
            return 'No license plates found in image.'

    except:
        # Handle any errors that occurred during the API request or response parsing
    
        return f'Error: API request failed with status code {response.status_code}\nMessage: {response.text}'

if __name__ == "__main__":

    image = 'E:/2nd phase/saved_img/Plate.jpg' # Define the path to the image

    # Get the number plate from the image
    numberPlate = recognize_plate(image)
    print(numberPlate)