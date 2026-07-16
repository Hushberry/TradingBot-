"""
=========================================================
KAI Smart Money AI
File: logger.py

Description:
------------
Configures the application's logging system.

Author: Vincent Chimezirim
Version: 1.0.0
=========================================================
"""

from __future__ import annotations
import logging
from config import LOG_DIR, LOG_FILE, LOG_LEVEL


#------------------------------------------------
# Create log directory if it doesn't exist
#------------------------------------------------

LOG_DIR.mkdir(parents=True, exist_ok=True)

#-------------------------------------------
# Configure logging
#-------------------------------------------

logging.basicConfig(
    level=getattr(logging, LOG_LEVEL),
    format="%(asctime)s | %(levelname)-8s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler(),
    ],
)

#------------------------------------------------
# Shared logger
#------------------------------------------------

logger = logging.getLogger("KAI")