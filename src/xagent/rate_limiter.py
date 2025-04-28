"""
Rate limiting functionality for the XAgent application.
Implements a token bucket algorithm for rate limiting API requests.
"""

import time
from typing import Optional
from threading import Lock

from .config import settings
from .logging import get_logger

logger = get_logger(__name__)

class RateLimiter:
    """Implements a token bucket rate limiter."""
    
    def __init__(self, requests_per_period: int, period_seconds: int):
        """Initialize the rate limiter.
        
        Args:
            requests_per_period: Maximum number of requests allowed in the period.
            period_seconds: Length of the period in seconds.
        """
        self.requests_per_period = requests_per_period
        self.period_seconds = period_seconds
        self.tokens = requests_per_period
        self.last_refill = time.time()
        self.lock = Lock()
        
    def _refill_tokens(self) -> None:
        """Refill tokens based on elapsed time."""
        now = time.time()
        time_passed = now - self.last_refill
        new_tokens = time_passed * (self.requests_per_period / self.period_seconds)
        
        if new_tokens > 0:
            self.tokens = min(self.requests_per_period, self.tokens + new_tokens)
            self.last_refill = now
            
    def acquire(self, tokens: int = 1) -> bool:
        """Try to acquire the specified number of tokens.
        
        Args:
            tokens: Number of tokens to acquire.
            
        Returns:
            bool: True if tokens were acquired, False otherwise.
        """
        with self.lock:
            self._refill_tokens()
            
            if self.tokens >= tokens:
                self.tokens -= tokens
                return True
            return False
            
    def wait(self, tokens: int = 1) -> None:
        """Wait until the specified number of tokens are available.
        
        Args:
            tokens: Number of tokens to wait for.
        """
        while not self.acquire(tokens):
            time.sleep(0.1)

# Create a global rate limiter instance
rate_limiter = RateLimiter(
    requests_per_period=settings.rate_limit_requests,
    period_seconds=settings.rate_limit_period
) 