try:
    from waterbutler import settings
except ImportError:
    settings = {}

config = settings.get('GOOGLEDRIVE_PROVIDER_CONFIG', {})


BASE_URL = config.get('BASE_URL', 'https://www.googleapis.com/drive/v2')
BASE_UPLOAD_URL = config.get('BASE_UPLOAD_URL', 'https://www.googleapis.com/upload/drive/v2')
DRIVE_IGNORE_VERSION = config.get('DRIVE_IGNORE_VERSION', '0000000000000000000000000000000000000')
