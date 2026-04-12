#!/usr/bin/env python3
import os
import sys
import subprocess
import tempfile
import unittest
from unittest.mock import patch
from generate_file import generate_random_file


class TestGenerateRandomFile(unittest.TestCase):
    """Test suite for generate_file.py"""

    def setUp(self):
        """Set up test fixtures"""
        self.test_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.test_dir, 'test_file.txt')

    def tearDown(self):
        """Clean up test files"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        if os.path.exists(self.test_dir):
            os.rmdir(self.test_dir)

    def test_file_creation(self):
        """Test that a file is created"""
        generate_random_file(self.test_file)
        self.assertTrue(os.path.exists(self.test_file), "File should be created")

    def test_file_content_length(self):
        """Test that the file contains 50 characters plus newline"""
        generate_random_file(self.test_file)
        with open(self.test_file, 'r') as f:
            content = f.read().strip()
        self.assertEqual(len(content), 50, "Content should be exactly 50 characters")

    def test_file_content_alphanumeric(self):
        """Test that the file content is alphanumeric"""
        generate_random_file(self.test_file)
        with open(self.test_file, 'r') as f:
            content = f.read().strip()
        self.assertTrue(content.isalnum(), "Content should be alphanumeric")

    def test_file_content_uniqueness(self):
        """Test that multiple runs generate different content"""
        # Generate first file
        generate_random_file(self.test_file)
        with open(self.test_file, 'r') as f:
            content1 = f.read().strip()

        # Generate second file
        test_file2 = os.path.join(self.test_dir, 'test_file2.txt')
        generate_random_file(test_file2)
        with open(test_file2, 'r') as f:
            content2 = f.read().strip()

        # Clean up second file
        os.remove(test_file2)

        # Content should be different (with very high probability)
        self.assertNotEqual(content1, content2, 
                          "Multiple runs should generate different content")

    def test_main_with_no_arguments(self):
        """Test that main script requires exactly one argument"""
        # Test by running the script as a subprocess
        script_dir = os.path.dirname(os.path.abspath(__file__))
        result = subprocess.run(
            [sys.executable, 'generate_file.py'],
            cwd=script_dir,
            capture_output=True,
            text=True
        )
        self.assertNotEqual(result.returncode, 0, 
                          "Script should exit with error when no arguments provided")
        self.assertIn("Использование", result.stdout, 
                     "Should display usage message")

    def test_file_has_newline(self):
        """Test that the file ends with a newline"""
        generate_random_file(self.test_file)
        with open(self.test_file, 'r') as f:
            content = f.read()
        self.assertTrue(content.endswith('\n'), "File should end with newline")


if __name__ == '__main__':
    unittest.main()
