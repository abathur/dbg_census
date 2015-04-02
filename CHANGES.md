Changes
=======

###1.0.1
    * Python 3 compatibility

###1.0.0
    * changed name from soe_api to dbg_census
    * main module changed name from soe_stats to dbg_census

###0.1.2
    * API base_url updated due to impending move of Census from census.soe.com to census.daybreakgames.com.
    * service_id set to default "example" which should work, but be rate-limited to 10 requests per minute per ip.
    * This will (in all likelihood) be the final release in this repository. The project will continue under the name dbg_census (https://github.com/abathur/dbg_census)

###0.1.1
    * API constructor now accepts api version string. For example at current the 'ps2' namespace also supports a more explicit specifier like 'ps2:v1' or 'ps2:v2'. While the default namespace is 'ps2', a constructor like ps2.Stats("v2") will allow you to specify a version string.
    * The version string may also be explicitly set with the api.version variable.

###0.1.0
    * Initial version
