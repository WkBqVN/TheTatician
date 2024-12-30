import logging

# Create a logger
logger = logging.getLogger("MyApp")
logger.setLevel(logging.DEBUG)

# Create handlers
file_handler = logging.FileHandler("app.log")
console_handler = logging.StreamHandler()

# Set level for handlers
file_handler.setLevel(logging.ERROR)
console_handler.setLevel(logging.DEBUG)

# Define a formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Add formatter to handlers
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Log messages
logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")
