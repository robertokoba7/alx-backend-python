#!/usr/bin/env python3

"""
This module contains unit and integration tests for utils.py and client.py
"""

import requests
import unittest
from unittest.mock import patch, Mock, PropertyMock, call
from parameterized import parameterized, parameterized_class
import utils
from utils import access_nested_map, get_json, memoize
from client import GithubOrgClient
import client
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """
    This class contains unit tests for the GithubOrgClient class
    """

    @parameterized.expand([
        ("google", {"google": True}),
        ("abc", {"abc": True})
    ])
    @patch('client.get_json')
    def test_org(self, org, expected, get_patch):
        """
        Test that the GithubOrgClient correctly sets its `org` attribute and
        that the `get_json` function is called with the correct URL.
        """
        # Set up mock to return expected value from `get_json`
        get_patch.return_value = expected

        # Create a GithubOrgClient instance and check that `org` is set
        # correctly
        x = GithubOrgClient(org)
        self.assertEqual(x.org, expected)

        # Check that `get_json` was called with the correct URL
        get_patch.assert_called_once_with("https://api.github.com/orgs/" + org)

    def test_public_repos_url(self):
        """
        Test that the `_public_repos_url` property of the GithubOrgClient
        correctly returns the URL for the public repositories of an organization.
        """
        expected = "www.yes.com"
        payload = {"repos_url": expected}
        to_mock = 'client.GithubOrgClient.org'
        with patch(to_mock, PropertyMock(return_value=payload)):
            cli = GithubOrgClient("x")
            self.assertEqual(cli._public_repos_url, expected)

    @patch('client.get_json')
    def test_public_repos(self, get_json_mock):
        """
        Test that the `public_repos` method of the GithubOrgClient correctly
        returns a list of public repositories for an organization, filtered by
        license if specified.
        """
        # Set up mock to return a list of repositories
        jeff = {"name": "Jeff", "license": {"key": "a"}}
        bobb = {"name": "Bobb", "license": {"key": "b"}}
        suee = {"name": "Suee"}
        to_mock = 'client.GithubOrgClient._public_repos_url'
        get_json_mock.return_value = [jeff, bobb, suee]

        # Create a GithubOrgClient instance and check that `public_repos`
        # returns the expected values
        with patch(to_mock, PropertyMock(return_value="www.yes.com")) as y:
            x = GithubOrgClient("x")

    with patch(to_mock, PropertyMock(return_value="www.yes.com")) as y:
        x = GithubOrgClient("x")
        self.assertEqual(x.public_repos(), ['Jeff', 'Bobb', 'Suee'])
        self.assertEqual(x.public_repos("a"), ['Jeff'])
        self.assertEqual(x.public_repos("c"), [])
        self.assertEqual(x.public_repos(45), [])
        get_json_mock.assert_called_once_with("www.yes.com")
        y.assert_called_once_with()


@parameterized.expand([
    ({'license': {'key': 'my_license'}}, 'my_license', True),
    ({'license': {'key': 'other_license'}}, 'my_license', False)
])
def test_has_license(self, repo, license, expected):
    """ Test the license checker """
    self.assertEqual(GithubOrgClient.has_license(repo, license), expected)


@classmethod
def setUpClass(cls):
    """ Prepare for testing """
    org = TEST_PAYLOAD[0][0]
    repos = TEST_PAYLOAD[0][1]
    org_mock = Mock()
    org_mock.json = Mock(return_value=org)
    cls.org_mock = org_mock
    repos_mock = Mock()
    repos_mock.json = Mock(return_value=repos)
    cls.repos_mock = repos_mock

    cls.get_patcher = patch('requests.get')
    cls.get = cls.get_patcher.start()

    options = {cls.org_payload["repos_url"]: repos_mock}
    cls.get.side_effect = lambda y: options.get(y, org_mock)


@classmethod
def tearDownClass(cls):
    """ Unprepare for testing """
    cls.get_patcher.stop()


def test_public_repos(self):
    """ Public repos test """
    y = GithubOrgClient("x")
    self.assertEqual(y.org, self.org_payload)
    self.assertEqual(y.repos_payload, self.repos_payload)
    self.assertEqual(y.public_repos(), self.expected_repos)
    self.assertEqual(y.public_repos("NONEXISTENT"), [])
    self.get.assert_has_calls([call("https://api.github.com/orgs/x"),
                               call(self.org_payload["repos_url"])])


def test_public_repos_with_license(self):
    """ Public repos with license test """
    y = GithubOrgClient("x")
    self.assertEqual(y.org, self.org_payload)
    self.assertEqual(y.repos_payload, self.repos_payload)
    self.assertEqual(y.public_repos(), self.expected_repos)
    self.assertEqual(y.public_repos("NONEXISTENT"), [])
    self.assertEqual(y.public_repos("apache-2.0"), self.apache2_repos)
    self.get.assert_has_calls([call("https://api.github.com/orgs/x"),
                               call(self.org_payload["repos_url"])])
