# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 12.3.1 for Mac OS X ARM (64-bit) (July 24, 2021)
# Date: Tue 11 Nov 2025 00:20:23


from object_library import all_decays, Decay
import particles as P


Decay_s1 = Decay(name = 'Decay_s1',
                 particle = P.s1,
                 partial_widths = {(P.e,P.e__tilde__):'(c1**2*Mds**2*cmath.sqrt(Mds**4 - 4*Mds**2*Me**2))/(8.*cmath.pi*abs(Mds)**3)',
                                   (P.mu,P.mu__tilde__):'(c1**2*Mds**2*cmath.sqrt(Mds**4 - 4*Mds**2*MMU**2))/(8.*cmath.pi*abs(Mds)**3)',
                                   (P.ta,P.ta__tilde__):'(c1**2*Mds**2*cmath.sqrt(Mds**4 - 4*Mds**2*MTA**2))/(8.*cmath.pi*abs(Mds)**3)'})

Decay_Snu = Decay(name = 'Decay_Snu',
                  particle = P.Snu,
                  partial_widths = {(P.A,P.Nu):'((-MNu**2 + Msnu**2)*(16*MNu**4*muNuN**2 - 32*MNu**2*Msnu**2*muNuN**2 + 16*Msnu**4*muNuN**2))/(32.*cmath.pi*abs(Msnu)**3)'})

Decay_Nu = Decay(name = 'Decay_Nu',
                 particle = P.Nu,
                 partial_widths = {(P.A,P.Snu):'((MNu**2 - Msnu**2)*(16*MNu**4*muNuN**2 - 32*MNu**2*Msnu**2*muNuN**2 + 16*Msnu**4*muNuN**2))/(32.*cmath.pi*abs(MNu)**3)'})

