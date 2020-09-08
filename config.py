from dotenv import load_dotenv
import os

load_dotenv()

config = {
  'CLIENT_TOKEN': os.getenv('CLIENT_TOKEN'),
  'DATABASE_HOST': os.getenv('DATABASE_HOST'),
  'DATABASE_PORT': int(os.getenv('DATABASE_PORT')),
  'DATABASE_USERNAME': os.getenv('DATABASE_USERNAME'),
  'DATABASE_PASSWORD': os.getenv('DATABASE_PASSWORD'),
  'DATABASE_NAME': os.getenv('DATABASE_NAME')
}