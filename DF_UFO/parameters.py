# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 12.3.1 for Mac OS X ARM (64-bit) (July 24, 2021)
# Date: Mon 10 Nov 2025 23:39:02



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
Znuc = Parameter(name = 'Znuc',
                 nature = 'external',
                 type = 'real',
                 value = 74,
                 texname = 'Z_{\\text{nuc}}',
                 lhablock = 'DPINPUTS',
                 lhacode = [ 3 ])

dnuc = Parameter(name = 'dnuc',
                 nature = 'external',
                 type = 'real',
                 value = 0.005069502007561487,
                 texname = '\\text{dnuc}',
                 lhablock = 'DPINPUTS',
                 lhacode = [ 5 ])

muNuN = Parameter(name = 'muNuN',
                  nature = 'external',
                  type = 'real',
                  value = 1.e-6,
                  texname = '\\text{muNuN}',
                  lhablock = 'FRBlock',
                  lhacode = [ 1 ])

Zm = Parameter(name = 'Zm',
               nature = 'external',
               type = 'real',
               value = 1,
               texname = '\\text{Zm}',
               lhablock = 'FRBlock',
               lhacode = [ 2 ])

ZA = Parameter(name = 'ZA',
               nature = 'external',
               type = 'real',
               value = 1,
               texname = '\\text{ZA}',
               lhablock = 'FRBlock',
               lhacode = [ 3 ])

Zpsi = Parameter(name = 'Zpsi',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{Zpsi}',
                 lhablock = 'FRBlock',
                 lhacode = [ 4 ])

Zxi = Parameter(name = 'Zxi',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{Zxi}',
                lhablock = 'FRBlock',
                lhacode = [ 5 ])

Zg = Parameter(name = 'Zg',
               nature = 'external',
               type = 'real',
               value = 1,
               texname = '\\text{Zg}',
               lhablock = 'FRBlock',
               lhacode = [ 6 ])

Me = Parameter(name = 'Me',
               nature = 'external',
               type = 'real',
               value = 0.000511,
               texname = '\\text{Me}',
               lhablock = 'MASS',
               lhacode = [ 11 ])

MMU = Parameter(name = 'MMU',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{MMU}',
                lhablock = 'MASS',
                lhacode = [ 13 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

Mproton = Parameter(name = 'Mproton',
                    nature = 'external',
                    type = 'real',
                    value = 171.,
                    texname = '\\text{Mproton}',
                    lhablock = 'MASS',
                    lhacode = [ 9000002 ])

Mds = Parameter(name = 'Mds',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{Mds}',
                lhablock = 'MASS',
                lhacode = [ 9000004 ])

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '0.3028619',
               texname = '\\text{ee}')

anuc = Parameter(name = 'anuc',
                 nature = 'internal',
                 type = 'real',
                 value = '111/(Me*Znuc**0.3333333333333333)',
                 texname = '\\text{anuc}')

