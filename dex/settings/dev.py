from .base import *

DATABASES = {
    "default": dj_database_url.config(
        default="postgresql://user:passwd@localhost:5432/db",
        conn_max_age=600,
    )
}
DATABASES["default"]["ATOMIC_REQUESTS"] = True