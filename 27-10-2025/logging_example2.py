import logging
import os
from datetime import datetime

# Create logs directory if missing
if not os.path.exists("logs"):
    os.makedirs("logs")

# Log file name with date stamp for uniqueness and retention
log_filename = f"logs/agenticai_{datetime.now().strftime('%Y-%m-%d')}.log"

logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    filemode="a"  # Append logs for each run
)

logger = logging.getLogger("agenticai")

logger.info("AGenticAI application started.")
# Example usage in your pipeline
logger.debug("Agent parsed request from user.")
logger.error("Failed to load config file.")
