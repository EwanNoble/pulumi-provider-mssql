# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs

__all__ = [
    'LoginServer',
    'LoginServerAzureLogin',
    'LoginServerLogin',
    'UserServer',
    'UserServerAzureLogin',
    'UserServerLogin',
]

@pulumi.output_type
class LoginServer(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "azureLogin":
            suggest = "azure_login"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in LoginServer. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        LoginServer.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        LoginServer.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 host: str,
                 azure_login: Optional['outputs.LoginServerAzureLogin'] = None,
                 login: Optional['outputs.LoginServerLogin'] = None,
                 port: Optional[str] = None):
        """
        :param str host: The host of the SQL Server. Changing this forces a new resource to be created.
        :param 'LoginServerAzureLoginArgs' azure_login: Azure AD login for managing the database resources. The attributes supported in the `azure_login` block is detailed below.
        :param 'LoginServerLoginArgs' login: SQL Server login for managing the database resources. The attributes supported in the `login` block is detailed below.
        :param str port: The port of the SQL Server. Defaults to `1433`. Changing this forces a new resource to be created.
        """
        pulumi.set(__self__, "host", host)
        if azure_login is not None:
            pulumi.set(__self__, "azure_login", azure_login)
        if login is not None:
            pulumi.set(__self__, "login", login)
        if port is not None:
            pulumi.set(__self__, "port", port)

    @property
    @pulumi.getter
    def host(self) -> str:
        """
        The host of the SQL Server. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "host")

    @property
    @pulumi.getter(name="azureLogin")
    def azure_login(self) -> Optional['outputs.LoginServerAzureLogin']:
        """
        Azure AD login for managing the database resources. The attributes supported in the `azure_login` block is detailed below.
        """
        return pulumi.get(self, "azure_login")

    @property
    @pulumi.getter
    def login(self) -> Optional['outputs.LoginServerLogin']:
        """
        SQL Server login for managing the database resources. The attributes supported in the `login` block is detailed below.
        """
        return pulumi.get(self, "login")

    @property
    @pulumi.getter
    def port(self) -> Optional[str]:
        """
        The port of the SQL Server. Defaults to `1433`. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "port")


@pulumi.output_type
class LoginServerAzureLogin(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "clientId":
            suggest = "client_id"
        elif key == "clientSecret":
            suggest = "client_secret"
        elif key == "tenantId":
            suggest = "tenant_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in LoginServerAzureLogin. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        LoginServerAzureLogin.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        LoginServerAzureLogin.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 client_id: str,
                 client_secret: str,
                 tenant_id: str):
        """
        :param str client_id: The client ID of the principal used to login to the SQL Server. Can also be sourced from the `MSSQL_CLIENT_ID` environment variable.
        :param str client_secret: The client secret of the principal used to login to the SQL Server. Can also be sourced from the `MSSQL_CLIENT_SECRET` environment variable.
        :param str tenant_id: The tanant ID of the principal used to login to the SQL Server. Can also be sourced from the `MSSQL_TENANT_ID` environment variable.
        """
        pulumi.set(__self__, "client_id", client_id)
        pulumi.set(__self__, "client_secret", client_secret)
        pulumi.set(__self__, "tenant_id", tenant_id)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> str:
        """
        The client ID of the principal used to login to the SQL Server. Can also be sourced from the `MSSQL_CLIENT_ID` environment variable.
        """
        return pulumi.get(self, "client_id")

    @property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> str:
        """
        The client secret of the principal used to login to the SQL Server. Can also be sourced from the `MSSQL_CLIENT_SECRET` environment variable.
        """
        return pulumi.get(self, "client_secret")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        The tanant ID of the principal used to login to the SQL Server. Can also be sourced from the `MSSQL_TENANT_ID` environment variable.
        """
        return pulumi.get(self, "tenant_id")


@pulumi.output_type
class LoginServerLogin(dict):
    def __init__(__self__, *,
                 password: str,
                 username: str):
        """
        :param str password: The password of the SQL Server login. Can also be sourced from the `MSSQL_PASSWORD` environment variable.
        :param str username: The username of the SQL Server login. Can also be sourced from the `MSSQL_USERNAME` environment variable.
        """
        pulumi.set(__self__, "password", password)
        pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter
    def password(self) -> str:
        """
        The password of the SQL Server login. Can also be sourced from the `MSSQL_PASSWORD` environment variable.
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def username(self) -> str:
        """
        The username of the SQL Server login. Can also be sourced from the `MSSQL_USERNAME` environment variable.
        """
        return pulumi.get(self, "username")


@pulumi.output_type
class UserServer(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "azureLogin":
            suggest = "azure_login"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in UserServer. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        UserServer.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        UserServer.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 host: str,
                 azure_login: Optional['outputs.UserServerAzureLogin'] = None,
                 login: Optional['outputs.UserServerLogin'] = None,
                 port: Optional[str] = None):
        """
        :param str host: The host of the SQL Server. Changing this forces a new resource to be created.
        :param 'UserServerAzureLoginArgs' azure_login: Azure AD login for managing the database resources. The attributes supported in the `azure_login` block is detailed below.
        :param 'UserServerLoginArgs' login: SQL Server login for managing the database resources. The attributes supported in the `login` block is detailed below.
        :param str port: The port of the SQL Server. Defaults to `1433`. Changing this forces a new resource to be created.
        """
        pulumi.set(__self__, "host", host)
        if azure_login is not None:
            pulumi.set(__self__, "azure_login", azure_login)
        if login is not None:
            pulumi.set(__self__, "login", login)
        if port is not None:
            pulumi.set(__self__, "port", port)

    @property
    @pulumi.getter
    def host(self) -> str:
        """
        The host of the SQL Server. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "host")

    @property
    @pulumi.getter(name="azureLogin")
    def azure_login(self) -> Optional['outputs.UserServerAzureLogin']:
        """
        Azure AD login for managing the database resources. The attributes supported in the `azure_login` block is detailed below.
        """
        return pulumi.get(self, "azure_login")

    @property
    @pulumi.getter
    def login(self) -> Optional['outputs.UserServerLogin']:
        """
        SQL Server login for managing the database resources. The attributes supported in the `login` block is detailed below.
        """
        return pulumi.get(self, "login")

    @property
    @pulumi.getter
    def port(self) -> Optional[str]:
        """
        The port of the SQL Server. Defaults to `1433`. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "port")


@pulumi.output_type
class UserServerAzureLogin(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "clientId":
            suggest = "client_id"
        elif key == "clientSecret":
            suggest = "client_secret"
        elif key == "tenantId":
            suggest = "tenant_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in UserServerAzureLogin. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        UserServerAzureLogin.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        UserServerAzureLogin.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 client_id: str,
                 client_secret: str,
                 tenant_id: str):
        """
        :param str client_id: The client ID of the principal used to login to the SQL Server. Can also be sourced from the `MSSQL_CLIENT_ID` environment variable.
        :param str client_secret: The client secret of the principal used to login to the SQL Server. Can also be sourced from the `MSSQL_CLIENT_SECRET` environment variable.
        :param str tenant_id: The tenant ID of the principal used to login to the SQL Server. Can also be sourced from the `MSSQL_TENANT_ID` environment variable.
        """
        pulumi.set(__self__, "client_id", client_id)
        pulumi.set(__self__, "client_secret", client_secret)
        pulumi.set(__self__, "tenant_id", tenant_id)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> str:
        """
        The client ID of the principal used to login to the SQL Server. Can also be sourced from the `MSSQL_CLIENT_ID` environment variable.
        """
        return pulumi.get(self, "client_id")

    @property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> str:
        """
        The client secret of the principal used to login to the SQL Server. Can also be sourced from the `MSSQL_CLIENT_SECRET` environment variable.
        """
        return pulumi.get(self, "client_secret")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        The tenant ID of the principal used to login to the SQL Server. Can also be sourced from the `MSSQL_TENANT_ID` environment variable.
        """
        return pulumi.get(self, "tenant_id")


@pulumi.output_type
class UserServerLogin(dict):
    def __init__(__self__, *,
                 password: str,
                 username: str):
        """
        :param str password: The password of the SQL Server login. Can also be sourced from the `MSSQL_PASSWORD` environment variable.
        :param str username: The username of the SQL Server login. Can also be sourced from the `MSSQL_USERNAME` environment variable.
        """
        pulumi.set(__self__, "password", password)
        pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter
    def password(self) -> str:
        """
        The password of the SQL Server login. Can also be sourced from the `MSSQL_PASSWORD` environment variable.
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def username(self) -> str:
        """
        The username of the SQL Server login. Can also be sourced from the `MSSQL_USERNAME` environment variable.
        """
        return pulumi.get(self, "username")


