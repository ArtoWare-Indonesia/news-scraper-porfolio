import logging
from datetime import datetime
from pathlib import Path


def setup_logger(level=logging.INFO):
    """Konfigurasi logger untuk seluruh aplikasi."""

    # Buat folder log
    log_dir = Path("output/logs")
    log_dir.mkdir(parents=True, exist_ok=True)

    # Nama file log dengan timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = log_dir / f"scraper_{timestamp}.log"

    logger = logging.getLogger()
    logger.setLevel(level)

    # Hindari handler ganda jika setup_logger() dipanggil lagi
    if logger.handlers:
        logger.handlers.clear()

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Tampilkan log ke terminal
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)

    # Simpan log ke file
    file_handler = logging.FileHandler(
        log_file,
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger