# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 12.3.1 for Mac OS X ARM (64-bit) (July 24, 2021)
# Date: Mon 10 Nov 2025 23:39:02


from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.e__tilde__, P.e, P.s1 ],
             color = [ '1' ],
             lorentz = [ L.FFS1 ],
             couplings = {(0,0):C.GC_1})

V_2 = Vertex(name = 'V_2',
             particles = [ P.mu__tilde__, P.mu, P.s1 ],
             color = [ '1' ],
             lorentz = [ L.FFS1 ],
             couplings = {(0,0):C.GC_1})

V_3 = Vertex(name = 'V_3',
             particles = [ P.ta__tilde__, P.ta, P.s1 ],
             color = [ '1' ],
             lorentz = [ L.FFS1 ],
             couplings = {(0,0):C.GC_1})

V_4 = Vertex(name = 'V_4',
             particles = [ P.e__tilde__, P.e, P.A ],
             color = [ '1' ],
             lorentz = [ L.FFV1 ],
             couplings = {(0,0):C.GC_1})

V_5 = Vertex(name = 'V_5',
             particles = [ P.mu__tilde__, P.mu, P.A ],
             color = [ '1' ],
             lorentz = [ L.FFV1 ],
             couplings = {(0,0):C.GC_1})

V_6 = Vertex(name = 'V_6',
             particles = [ P.ta__tilde__, P.ta, P.A ],
             color = [ '1' ],
             lorentz = [ L.FFV1 ],
             couplings = {(0,0):C.GC_1})

V_7 = Vertex(name = 'V_7',
             particles = [ P.Proton__tilde__, P.Proton, P.A ],
             color = [ '1' ],
             lorentz = [ L.FFV1 ],
             couplings = {(0,0):C.GC_1})

V_8 = Vertex(name = 'V_8',
             particles = [ P.Snu__tilde__, P.Nu, P.A ],
             color = [ '1' ],
             lorentz = [ L.FFV2 ],
             couplings = {(0,0):C.GC_2})

V_9 = Vertex(name = 'V_9',
             particles = [ P.Nu__tilde__, P.Snu, P.A ],
             color = [ '1' ],
             lorentz = [ L.FFV2 ],
             couplings = {(0,0):C.GC_2})

