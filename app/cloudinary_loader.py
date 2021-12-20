from config import CLOUDINARY_API_ENV_VAR, CLOUDINARY_API_KEY, CLOUDINARY_API_SECRET
import cloudinary

class CloudinaryLoader:
    def __init__(self):
        self.api_key = CLOUDINARY_API_KEY
        self.api_secret = CLOUDINARY_API_SECRET
        self.api_env_var = CLOUDINARY_API_ENV_VAR

        cloudinary.config(
            cloud_name="danangbkdn",
            api_key=self.api_key,
            api_secret=self.api_secret
        )