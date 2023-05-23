#!/usr/bin/env python3
"""
Test file for github org client
"""
from parameterized import parameterized
import unittest
from client import GithubOrgClient
from unittest.mock import patch

class TestGithubOrgClient(unittest.TestCase):
    """
    Implementation of github org client class
    """

    @parameterized.expand([
        ("google", "google"),
        ("abc", "abc")
    ])
    @patch('client.get_json')
    def test_org(self, _: str, org_name: str, mock_get_json):
        """
        Tests that GithubOrgClient.org returns correct value
        """
        mock_get_json.return_value = {"repos_url": "https://api.github.com/orgs/{}/repos".format(org_name)}
        gitclient = GithubOrgClient(org_name)
        org_repo = gitclient.org
        self.assertEqual(org_repo, {"repos_url": "https://api.github.com/orgs/{}/repos".format(org_name)})
        mock_get_json.assert_called_with(gitclient.ORG_URL.format(org=org_name))
        
        