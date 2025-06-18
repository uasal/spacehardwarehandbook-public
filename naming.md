<!--- Naming Standards --->

## Criteria For Naming Assemblies
Consistent naming of mechancial components is key for tracking parts and maintaining a clear folder structure for design files.

For mechanical assemblies we have adopted the approach below. In the example, a subassembly such as the JWST aft-optics assembly (AOA) houses a fictitous Extra-Solar Coronagaph instrument 

1. The Assembly will be represented by an alphanumeric string, e.g., XXX-XXX-####, where X is capital
letter and # is a number from 0-9.
a. An additional dash and 3-character string of numbers may be used to account for
assemblies containing multiple similar configurations of parts or subassemblies, e.g., XXX-####-###
b. Major assemblies are numbered XXX-#####. 
c. The file location of a part is described by the part number. e.g. AOA-STC-1000 is located in the
folder named "STC" within the folder "AOA". 
2. The first set of characters in the alphanumeric string, XXX, will be a human readable acronym
or abbreviation describing the major assembly, e.g., AOA for Aft Optics Assembly.
3. The second set of characters, XXX, will be will be a human readable acronym
or abbreviation describing the subassembly, e.g., ESC for Extra Solar Coronagraph.
4. The third set of characters, ####, will be chosen based on hierarchy within the sub-assemblies
and type. 
a. The top subassembly will be represented by 1000, and its sub-assemblies and components
are distinguished numerically, so that 11##, 12## and 13## are sub-assemblies of 1000.
Likewise, 111#, 112# and 113# are sub-assemblies/components of the 11## sub-
assembly.
b. Electrical assemblies will have the suffix begin with a capital E, e.g., -E####
5. Within a level of sub-assemblies, the highest numbers are used for piece parts and cabling, e.g.,
19## for piece parts and 18## for cabling.
6. The entire Part/Assembly/Drawing alphanumeric string for an optical mount in ESC for example
would be, in 002 configuration:
AOA-ESC-1210-002 
