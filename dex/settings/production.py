import os

import environ

from .base import *

env = environ.Env()

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": env.db("DATABASE_URL"),
}
DATABASES["default"]["ATOMIC_REQUESTS"] = True

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#default-from-email
DEFAULT_FROM_EMAIL = env(
    "DJANGO_DEFAULT_FROM_EMAIL",
    default="Vaidyuti Dev Backend <vaidyuti-dev-backend@rithviknishad.dev>",
)

# https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = env("DJANGO_SERVER_EMAIL", default=DEFAULT_FROM_EMAIL)

# Twilio SendGrid
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.smtp.EmailBackend", EMAIL_HOST="smtp.sendgrid.net"
)
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "apikey"
EMAIL_HOST_PASSWORD = os.environ.get("SENDGRID_API_KEY")
