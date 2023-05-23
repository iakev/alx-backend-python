#!/usr/bin/env python3
"""
Test file for github org client
"""
from parameterized import parameterized
import unittest
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock


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
        mock_url = "https://api.github.com/orgs/{}/repos".format(org_name)
        mock_get_json.return_value = {"repos_url": mock_url}
        gitclient = GithubOrgClient(org_name)
        org_repo = gitclient.org
        self.assertEqual(org_repo, {"repos_url": mock_url})
        mock_get_json.assert_called_with
        (gitclient.ORG_URL.format(org=org_name))

    def test_public_repos_url(self):
        """
        method to unit test GithubOrgClient._public_repos_url
        """
        mock_url = "https://api.github.com/orgs/google/repos"
        test_payload = {"repos_url": mock_url}
        with patch('test_client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = test_payload
            git_client = GithubOrgClient("google")
            url = git_client._public_repos_url
            self.assertEqual(url, test_payload["repos_url"])
