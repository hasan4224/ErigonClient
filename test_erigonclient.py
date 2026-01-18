# test_erigonclient.py
"""
Tests for ErigonClient module.
"""

import unittest
from erigonclient import ErigonClient

class TestErigonClient(unittest.TestCase):
    """Test cases for ErigonClient class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ErigonClient()
        self.assertIsInstance(instance, ErigonClient)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ErigonClient()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
