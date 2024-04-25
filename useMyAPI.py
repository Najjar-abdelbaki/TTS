import requests

#  النص لي نحبو نحولوه
data = {
    'text': 'مرحبًا، كيف حالك؟'
}

# API endpoint URL
api_url = 'https://najjara.pythonanywhere.com/api/convert'

# Send a POST request for text-to-speech
response = requests.post(api_url, json=data)


if response.status_code == 200:
    with open('audio.mp3', 'wb') as file:
        file.write(response.content)
    print("done!")
    print("The audio file has been saved as 'audio.mp3'.")
else:
    print("An error occurred while converting text to speech. Please try again.")