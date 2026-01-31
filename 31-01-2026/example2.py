import logging
import os
from datetime import datetime

class AgentLogger:
    """
    Production-grade logger for agentic AI projects.
    Creates a log file per instance with datetime in filename.
    Logs include timestamp, log level, module, and message.
    """
    def __init__(self, log_dir: str = "logs", agent_name: str = "agent") -> None:
        """
        Initialize the AgentLogger.
        Args:
            log_dir (str): Directory to store log files. Defaults to 'logs'.
            agent_name (str): Name of the agent for log file naming. Defaults to 'agent'.
        """
        os.makedirs(log_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_filename = f"{agent_name}_{timestamp}.log"
        log_path = os.path.join(log_dir, log_filename)
        self.logger = logging.getLogger(f"{agent_name}_{timestamp}")
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter(
            fmt="%(asctime)s | %(levelname)s | %(module)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        file_handler = logging.FileHandler(log_path)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        # Optional: also log to console
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

    def info(self, message: str) -> None:
        """
        Log an informational message.
        Args:
            message (str): The message to log.
        """
        self.logger.info(message)

    def error(self, message: str) -> None:
        """
        Log an error message.
        Args:
            message (str): The error message to log.
        """
        self.logger.error(message)

    def warning(self, message: str) -> None:
        """
        Log a warning message.
        Args:
            message (str): The warning message to log.
        """
        self.logger.warning(message)

    def debug(self, message: str) -> None:
        """
        Log a debug message.
        Args:
            message (str): The debug message to log.
        """
        self.logger.debug(message)

    def critical(self, message: str) -> None:
        """
        Log a critical message.
        Args:
            message (str): The critical message to log.
        """
        self.logger.critical(message)


if __name__ == "__main__":
    print(__name__)
    log = AgentLogger(agent_name="my_agent")
    log.info("This is an informational message.")
    log.error("This is an error message.")
    log.warning("This is a warning message.")
    log.debug("This is a debug message.")
    log.critical("This is a critical message.")