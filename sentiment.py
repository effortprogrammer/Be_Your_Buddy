import os, requests, uuid, json

# Don't forget to replace with your Cog Services subscription key!
subscription_key = 'subscription_key' 
# Our Flask route will supply four arguments: input_text, input_language,
# output_text, output_language.
# When the run sentiment analysis button is pressed in our Flask app,
# the Ajax request will grab these values from our web app, and use them
# in the request. See main.js for Ajax calls.

def get_sentiment(input_text, input_language, output_text, output):
    constructed_url = 'https://westus2.api.cognitive.microsoft.com/text/analytics/v3.1-preview.1/sentiment'

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = {
        'documents': [
            {
                'language': input_language,
                'id': '1',
                'text': input_text
            },
        ]
    }
    response = requests.post(constructed_url, headers=headers, json=body)
    return response.json()