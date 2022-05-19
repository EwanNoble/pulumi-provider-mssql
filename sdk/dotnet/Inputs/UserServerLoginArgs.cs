// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Mssql.Inputs
{

    public sealed class UserServerLoginArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The password of the SQL Server login. Can also be sourced from the `MSSQL_PASSWORD` environment variable.
        /// </summary>
        [Input("password", required: true)]
        public Input<string> Password { get; set; } = null!;

        /// <summary>
        /// The username of the SQL Server login. Can also be sourced from the `MSSQL_USERNAME` environment variable.
        /// </summary>
        [Input("username", required: true)]
        public Input<string> Username { get; set; } = null!;

        public UserServerLoginArgs()
        {
        }
    }
}
