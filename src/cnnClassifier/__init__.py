import os
import sys
import logging

# This file is used for creating custom logging
# Default logging.basicConfig() sends everything to console or a single file.
#   In production, you may want:
#     - Errors in one file (error.log).
#     - All activity in another file (app.log)
#     - Info-level logs in console.

logging_str = "[%(asctime)s : %(levelname)s : %(module)s : %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("cnnClassifierLogger")
