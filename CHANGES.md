Changes
=======

###0.1.1
    * API constructor now accepts api version string. For example at current the 'ps2' namespace also supports a more explicit specifier like 'ps2:v1' or 'ps2:v2'. While the default namespace is 'ps2', a constructor like ps2.Stats("v2") will allow you to specify a version string.
    * The version string may also be explicitly set with the api.version variable.

###0.1.0
    * Initial version
