PCB and Circuit Design Basics
==============================

The original source of this document is the Steward Space Telescope Program's Space Coronagraph Design Guide.

Electronics Build
-------------------

Select parts based on `ElectronicComponentSelectionCriteria.md` (tbd).

PCB Manufacturing
^^^^^^^^^^^^^^^^^

The cost of catching manufacturing errors early is far lower than having cheap prototypes hold us back.

Baseline PCB manufacturing is high reliability IPC 6012 Class 3 and soldered to IPC J-STD-001, Space addendum optional. Where practical, ESA and NASA design rules for printed circuit boards shall also be followed.

PCB Inspection
^^^^^^^^^^^^^^

Flight and protoflight boards will be inspected by the manufacturer to IPC 600-A Class 3, and assemblies to IPC-A-610 class 3. All boards will additionally be inspected and photographed by a UA technician or engineer.

Bake out
^^^^^^^^

Before conformal coating the electronics should be baked out to remove moisture and volatiles. Following the CubeSat standard `LSP-REQ-317.01 <https://www.nasa.gov/pdf/627972main_LSP-REQ-317_01A.pdf>`__:

  | Min. Temp 70°C 
  | (Maximum bake out temperature set to same maximum temperature for thermal cycle test for consistency, assuming bake out would be performed during same vacuum exposure.)
  | Cycles = 1
  | Dwell Time = Min. 3 hour after thermal stabilization
  | Transition = < 5° C/minute
  | Vacuum = 1x10-4 Torr

After bake out exposure to moisture should be minimized.

Conformal Coating
^^^^^^^^^^^^^^^^^

Flight PCB should be conformal coated to discourage tin whisker formation, offer some protection against short circuits from FOD, and prevent arc-over from high voltage traces/connections. Parylene is often considered the gold standard for this purpose but is expensive and will likely need to be performed by an external vendor. For prototype purposes, a low outgassing alternative or no conformal coating should be investigated but margins for conformal coating must be maintained.

Unless specified otherwise, the default conformal coating is Arathane 5750 A/B (LV) (TBR, low outgassing but known to cause UV degradation, and quantities with a direct path to the optical assemblies should be minimized, see Hahne, A. (2012). Investigation on GOME-2 throughput degradation Final Report. ESTEC. Retrieved from `<https://www-cdn.eumetsat.int/files/2020-04/pdf_gome_thru_deg_esa.pdf>`__).

The coating should be applied by the board house. 
  
  "Let the board house do it and my own touch-ups, though. I make a batch of 5750, and make a solution of 50% MEK and 50% toluene by volume, then use hat to thin the 5750 50-50 by weight."
  
  David Hamara, Personal Communication

Soldering considerations
^^^^^^^^^^^^^^^^^^^^^^^^

- Each joint should be inspected via x-ray ("100% coverage") following IPC J-STD-001E or equivalent aerospace solder standard.
- Leaded (Pb/Sn) solder shall be used for reliability in all joints, minimizing whiskers and enabling future rework.

High Voltage Design Considerations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Design and handling should follow `NASA Handbook 4007 best practices for 50-250V circuits <https://standards.nasa.gov/standard/NASA/NASA-HDBK-4007>`__, section 7.4.2.1-7.4.2.2.

Spacecraft Charging Considerations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In LEO the primary concern is external charging due to the ambient plasma, design of solar panels and the external structure should be informed by the appropriate NASA Handbook [1]_.

Because of the highly ESD sensitive nature of the MEMS device and the unknown range of potential orbits, we require implement GEO-level internal ESD protections.

Internal Electronics
----------------------

Payload electronics should follow "Internal ESD Design Guidelines- Section 3.2.3" of the `"Guide to mitigating spacecraft charging" <https://descanso.jpl.nasa.gov/SciTechBook/series3/ChgingBook--110629-RibbonC.pdf>`__ particularly noting the following:

Voltage Stress
^^^^^^^^^^^^^^

The electric field stress in dielectrics should be below :math:`4 \times 4000` V/mm in any material or gap [2]_ and gap voltage stresses below 400V/mm [1]_.

Filtering
^^^^^^^^^

A basic filter circuit to protect from internal ESD shorts [2]_:

  The filter should anticipate a pulse on the order of 20 ns wide. As a rough example, filtering should protect against a 20-pF capacitance charged with 100 nC (about 5 kV stress, 250 :math:`\mu` J)

This is comparable to human body model static discharges (200nC at 2kV in 150 ns [3]_).

Bleedpaths
^^^^^^^^^^

Metal surfaces should have bleedpaths to ground [2]_:

  Circuit boards should be designed so that any metal area greater than 0.3 cm :math:`^2` should also have a bleed path with the same ESD grounding limits of 0 to :math:`10 M \Omega` resistance to ground. Circuit boards should be designed so that there will be no open (unused) surface areas greater than 0.3 cm\ :math:`^2`. Otherwise, place a metal land that is ESD grounded with 0 to 10 M :math:`\Omega` resistance to ground in the unused dielectric area.

Insulation
^^^^^^^^^^
See `NEPP insulation guide <https://nepp.nasa.gov/npsl/wire/insulation_guide.htm>`__, default wiring will be PTFE, Tefzel or Polyimide (Kapton).


.. [1] `NASA Handbook 4007 best practices for 50-250V circuits <https://standards.nasa.gov/standard/NASA/NASA-HDBK-4007>`__
.. [2] `<https://descanso.jpl.nasa.gov/SciTechBook/series3/ChgingBook--110629-RibbonC.pdf>`__
.. [3] `Design considerations for system-level ESD circuit protection, <https://www.ti.com/lit/an/slyt492/slyt492.pdf?ts=1751025356944>`__ R. Liang