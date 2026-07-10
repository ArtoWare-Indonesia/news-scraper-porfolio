import logging


def setup_logger(level=logging.INFO):
    """Konfigurasi logger untuk seluruh aplikasi."""

    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    return logging.getLogger()
