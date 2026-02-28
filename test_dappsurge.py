# test_dappsurge.py
"""
Tests for DAppSurge module.
"""

import unittest
from dappsurge import DAppSurge

class TestDAppSurge(unittest.TestCase):
    """Test cases for DAppSurge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DAppSurge()
        self.assertIsInstance(instance, DAppSurge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DAppSurge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
