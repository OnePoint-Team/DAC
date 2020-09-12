from gino.ext.starlette import Gino
from core.factories import settings
from ssl import create_default_context


if not settings.DEBUG:
    ssl_object = create_default_context(cafile=settings.SSL_CERT_FILE)
    db: Gino = Gino(dsn=settings.DATABASE_URL, echo=False, ssl=ssl_object,
                    pool_min_size=3, pool_max_size=20, retry_limit=5, retry_interval=5)
else:

    db: Gino = Gino(dsn=settings.DATABASE_URL)