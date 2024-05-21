A summary of radiation types that may impact the system:

Total Ionizing Dose 
Since TID is independent of radiation type, the energy absorbed from gamma rays should be equivalent to the energy absorbed from protons. TID is a long-term ionization effect that primarily impacts carbon-based materials and active piece parts. Damage includes increased leakage current, changes in gain, changes in voltage references, etc. The magnitude of the damage is correlated with dose and TID effects are usually not seen until late in a part’s lifetime with a gradual degradation of functionality becoming apparent before complete failure. 
Shielding allows for partial mitigation of TID; however, there is a point of diminishing return, especially when considering weight and cost. For aluminum, which can be used to block all but gamma radiation, beyond 5mm to 10mm of shielding, there is little effect on dose. Other materials, such as copper, tantalum and lead, can be more effective at shielding, but also produce additional Bremsstrahlung radiation, or electromagnetic radiation emitted when a charged particle is decelerated upon striking against another charged particle—negating the advantage of the materials. This can be countered by using composite shields, but the design effort is higher. 

Single Event Effects 
Where TID is a gradual degradation, single event effects (SEEs) are individual events which occur when a single incident ionizing particle deposits enough energy to cause a consequence in a device. Testing for SEE events is generally more expensive and less accessible than TID testing, and therefore is often an accepted risk. SEE can be separated into hard SEE and soft SEE.  
Hard SEE causes permanent physical damage to an electrical component, such as creating a conductive path to short circuit a component (Single Event Latchup) and cause damage, create a high current flow which causes local heating and damage (Single Event Gate Rupture), or create a short circuit and cause physical damage in the form of impact-crater-like features where the semiconductor has vaporized and exploded out (Single Event Burnout). It is usually not the particle itself causing destruction of the device, but the high electrical energy being controlled by the impacted device that causes destruction. The best way to combat hard SEE is to power down electronics during space weather events. 
Soft SEE causes undesired operation without damage to the component the particle passes through. However, undesired operation may cause damage to other components such as if ionizing radiation deposits enough charge to change the state of a memory element or logic circuit (Single Event Upset), or state-machine logic in complex IC changes state as a result of radiation, potentially reaching a normally unreachable state (Single Event Function Interrupt), or in components such as analog or power circuits the component briefly operates erratically before returning to normal operation (Single Event Transient). Soft SEE is only a concern when a device is powered on, unless the device uses bit flips, which can be affected even when a component is powered down. 


Radiation effects and COTS electronics reading list:

Sinclair, D., & Dyer, J. (2013). Radiation Effects and COTS Parts in SmallSats. In Small Satellite Conference (p. 12). 
Logan, Utah, USA. Retrieved from https://digitalcommons.usu.edu/cgi/viewcontent.cgi?article=2934&context=smallsat


Nikulainen, M., & Tonicello, F. (n.d.). Utilization of COTS in ESA Missions, 20.
https://nepp.nasa.gov/workshops/etw2021/talks/17-JUN-21_Thur/1045_Nikulainen_Tonicello-Utilisation-of-COTS-in-ESA-Missions.pdf

Becker, H. N., Dolphin, M. D., Thorbourn, D. O., Alexander, J. W., & Salomon, P. M. (2008). Commercial sensory survey radiation testing progress report. Pasadena, CA: Jet Propulsion Laboratory, National Aeronautics and Space Administration. Retrieved from https://trs.jpl.nasa.gov/bitstream/handle/2014/40825/08-22.pdf?sequence=1


Lietner, J. (2022, May 12). Phasing in COTS EEE Parts in NASA [Text]. Retrieved August 29, 2022, from http://www.nasa.gov/smallsat-institute/phasing-in-cots-eee-parts-in-nasa. [local PDF copy](attachments/nasa-cotsphasing-final.pdf)

Christian Haughwout, et al.  (2023). Compact deformable mirror driver electronics for risk tolerant astrophysics missions. Proceedings Volume 12677, Astronomical Optics: Design, Manufacture, and Test of Space and Ground Systems IV; 1267706https://doi.org/10.1117/12.2677714

---

To go to the radiation reports directory:

[Radiation Reports](/reports/radiation/readme.md)
