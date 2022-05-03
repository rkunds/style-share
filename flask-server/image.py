from google.cloud import storage
import random
import string

bucket_name = "styled-images"
storage_client = storage.Client.from_service_account_json("./config/creds.json")
bucket = storage_client.get_bucket(bucket_name)

alphabet = string.ascii_lowercase + string.digits

def upload_to_bucket(image):
    name = ''.join(random.choice(alphabet) for i in range(10)) + ".png"

    blob = bucket.blob(name)
    blob.upload_from_file(image, content_type='image/png')

    return blob.public_url