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
        Method to unit test GithubOrgClient._public_repos_url
        """
        mock_url = "https://api.github.com/orgs/google/repos"
        test_payload = {"repos_url": mock_url}
        with patch('test_client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = test_payload
            git_client = GithubOrgClient("google")
            url = git_client._public_repos_url
            self.assertEqual(url, test_payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """
        Method to unit test GithubOrgClient.public_repos
        """
        mock_url = "https://api.github.com/orgs/google/repos"
        payload = {mock_url: [{"name": "google/episodes.dart", "license": {
          "key": "bsd-3-clause",
          "name": "BSD 3-Clause \"New\" or \"Revised\" License",
          "spdx_id": "BSD-3-Clause",
          "url": "https://api.github.com/licenses/bsd-3-clause",
          "node_id": "MDc6TGljZW5zZTU="
        }}, {"name": "cpp-netlib", "license": None},
            {"name": "ios-webkit-debug-proxy"}]}
        mock_get_json.return_value = payload[mock_url]
        with patch('test_client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repo:
            mock_public_repo.return_value = mock_url
            gitcli = GithubOrgClient("google")
            names_list = gitcli.public_repos()
            expected_list = ["google/episodes.dart",
                             "cpp-netlib", "ios-webkit-debug-proxy"]
            self.assertEqual(names_list, expected_list)
            mock_public_repo.assert_called_once()
        mock_get_json.assert_called_once()
