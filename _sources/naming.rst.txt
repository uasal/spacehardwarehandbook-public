Criteria For Naming Assemblies
=================================

Consistent naming of mechancial components is key for tracking parts and maintaining a clear folder structure for design files.

For mechanical assemblies we have adopted the approach below. In the example, a Space Telescope Program runs a Versatile CubeSat Telescope (VCT) which contains an aft-optics assembly (AOA) that  houses a fictitous Extra-Solar Coronagraph (ESC) instrument.

1. The Assembly will be represented by an alphanumeric string, e.g., XXX-XXX-XX###, where X is capital letter and # is a number from 0-9.

2. The first 3-character string is a human readable acronnym or abbreviation describing the project or mission, e.g., AOA-XXX-XX###.

3. The second 3-character string is a human readable acronym or abbreviation describing a specific instrument or element, e.g., AOA-ESC-XX###.

4. The two capital letters in the 5-character string indicate the development category and engineering subset, e.g., AOA-ESC-FA###.

   a. First character is a capital letter indicating development category, e.g., F for Flight Ready, G for Ground Support Equipment.
   b. Second character is a capital letter indicating the engineering subset, e.g., A for Assembly, P for Part.
   c. Capital letters can be added to track additional categories or subsets, e.g., adding E for Electronics or T for Test Prototype.

5. The three numbers in the 5-character string indicate a specific assembly number within the indicated category, e.g., AOA-ESC-FA123.

6. An additional dash and 2-character string of numbers may be used to account for assemblies containing multiple similar configurations of parts or subassemblies, e.g., XXX-XXX-XX###-##.

7. Subsets of numbers may be reserved for specific subcategories. Alternatively, numbers may be assigned sequentially. e.g., only optical mounts are assigned an assembly number between AOA-ESC-[FA100] and AOA-ESC-[FA199].

8. Alphanumeric strings may be abbreviated depending on project or document organization, e.g., XXX-XXX-XX###-## shortened to XXX-XX### or XX###.

9. The file location of a part is described by the part number, e.g. AOA-ESC-FA123 is located in the folder named "ESC” within the folder “AOA”.

=================================

Examples

AOA-ESC-FA227 indicates the 227th flight assembly for the Extra Solar Coronagraph instrument on the JWST Aft Optics Assembly. 

AOA-ESC-FP238 indicates the 238th flight part for the Extra Solar Coronagraph instrument on the JWST Aft Optics Assembly. 

AOA-ESC-FA086-01 and AOA-ESC-FA086-02 indicates the 86th flight assembly for the Extra Solar Coronagraph instrument on the JWST Aft Optics Assembly. This assembly has two unique configurations, configuration 01 and configuration 02.
