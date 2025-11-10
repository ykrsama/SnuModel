# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 12.3.1 for Mac OS X ARM (64-bit) (July 24, 2021)
# Date: Mon 10 Nov 2025 23:39:02


from __future__ import division
from object_library import all_particles, Particle
import parameters as Param

import propagators as Prop

Snu = Particle(pdg_code = 9000001,
               name = 'Snu',
               antiname = 'Snu~',
               spin = 2,
               color = 1,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'Snu',
               antitexname = 'Snu~',
               charge = 0,
               LeptonNumber = 1)

Snu__tilde__ = Snu.anti()

e = Particle(pdg_code = 11,
             name = 'e',
             antiname = 'e~',
             spin = 2,
             color = 1,
             mass = Param.Me,
             width = Param.ZERO,
             texname = 'e',
             antitexname = 'e~',
             charge = 1,
             LeptonNumber = 1)

e__tilde__ = e.anti()

mu = Particle(pdg_code = 13,
              name = 'mu',
              antiname = 'mu~',
              spin = 2,
              color = 1,
              mass = Param.MMU,
              width = Param.ZERO,
              texname = 'mu',
              antitexname = 'mu~',
              charge = 1,
              LeptonNumber = 1)

mu__tilde__ = mu.anti()

ta = Particle(pdg_code = 15,
              name = 'ta',
              antiname = 'ta~',
              spin = 2,
              color = 1,
              mass = Param.MTA,
              width = Param.ZERO,
              texname = 'ta',
              antitexname = 'ta~',
              charge = 1,
              LeptonNumber = 1)

ta__tilde__ = ta.anti()

Proton = Particle(pdg_code = 9000002,
                  name = 'Proton',
                  antiname = 'Proton~',
                  spin = 2,
                  color = 1,
                  mass = Param.Mproton,
                  width = Param.ZERO,
                  texname = 'Proton',
                  antitexname = 'Proton~',
                  charge = 1,
                  LeptonNumber = 0)

Proton__tilde__ = Proton.anti()

Nu = Particle(pdg_code = 9000003,
              name = 'Nu',
              antiname = 'Nu~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 'Nu',
              antitexname = 'Nu~',
              charge = 0,
              LeptonNumber = 1)

Nu__tilde__ = Nu.anti()

A = Particle(pdg_code = 22,
             name = 'A',
             antiname = 'A',
             spin = 3,
             color = 1,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'A',
             antitexname = 'A',
             charge = 0,
             LeptonNumber = 0)

s1 = Particle(pdg_code = 9000004,
              name = 's1',
              antiname = 's1',
              spin = 1,
              color = 1,
              mass = Param.Mds,
              width = Param.ZERO,
              texname = 's1',
              antitexname = 's1',
              charge = 0,
              LeptonNumber = 0)

