# -*- coding: utf-8 -*-
"""
pMuTT.test_pMuTT_reactions
Tests for pMuTT module
"""

import unittest
from pMuTT.empirical.nasa import Nasa
from pMuTT.reaction import Reaction, Reactions

class TestReactions(unittest.TestCase):
    def setUp(self):
        self.species_dict = {
            'H2O': Nasa(name='H2O', T_low=200., T_mid=1000., T_high=3500.,
                        elements={'H': 2, 'O': 1},
                        a_low=[4.19864056E+00, -2.03643410E-03, 6.52040211E-06, 
                               -5.48797062E-09, 1.77197817E-12, -3.02937267E+04,
                               -8.49032208E-01],
                        a_high=[3.03399249E+00, 2.17691804E-03, -1.64072518E-07,
                                -9.70419870E-11, 1.68200992E-14,
                                -3.00042971E+04, 4.96677010E+00]),
            'H2': Nasa(name='H2', T_low=200., T_mid=1000., T_high=3500.,
                       elements={'H': 2},
                       a_low=[2.34433112E+00, 7.98052075E-03, -1.94781510E-05,
                              2.01572094E-08, -7.37611761E-12, -9.17935173E+02,
                              6.83010238E-01],
                       a_high=[3.33727920E+00, -4.94024731E-05, 4.99456778E-07, 
                               -1.79566394E-10, 2.00255376E-14, -9.50158922E+02,
                               -3.20502331E+00]),
            'O2': Nasa(name='O2', T_low=200., T_mid=1000., T_high=3500.,
                       elements={'O': 2},
                       a_low=[3.78245636E+00, -2.99673416E-03, 9.84730201E-06, 
                              -9.68129509E-09, 3.24372837E-12, -1.06394356E+03,
                              3.65767573E+00],
                       a_high=[3.28253784E+00, 1.48308754E-03, -7.57966669E-07,
                               2.09470555E-10, -2.16717794E-14, -1.08845772E+03,
                               5.45323129E+00]),
            'O': Nasa(name='O', T_low=200., T_mid=1000., T_high=3500.,
                      elements={'O': 1},
                      a_low=[3.16826710E+00, -3.27931884E-03, 6.64306396E-06, 
                             -6.12806624E-09, 2.11265971E-12, 2.91222592E+04,
                             2.05193346E+00],
                      a_high=[2.56942078E+00, -8.59741137E-05, 4.19484589E-08, 
                              -1.00177799E-11, 1.22833691E-15, 2.92175791E+04,
                              4.78433864E+00]),
            'H': Nasa(name='H', T_low=200., T_mid=1000., T_high=3500.,
                      elements={'H': 1},
                      a_low=[2.50000000E+00, 7.05332819E-13, -1.99591964E-15,
                             2.30081632E-18, -9.27732332E-22, 2.54736599E+04,
                             -4.46682853E-01],
                      a_high=[2.50000001E+00, -2.30842973E-11, 1.61561948E-14,
                              -4.73515235E-18, 4.98197357E-22, 2.54736599E+04, 
                              -4.46682914E-01]),
            'OH': Nasa(name='OH', T_low=200., T_mid=1000., T_high=3500.,
                       elements={'O': 1, 'H': 1},
                       a_high=[3.09288767E+00, 5.48429716E-04, 1.26505228E-07, 
                               -8.79461556E-11, 1.17412376E-14, 3.85865700E+03,
                               4.47669610E+00],
                       a_low=[3.99201543E+00, -2.40131752E-03, 4.61793841E-06,
                              -3.88113333E-09, 1.36411470E-12, 3.61508056E+03,
                              -1.03925458E-01])
        }
        self.reactions = Reactions(reactions=[
            Reaction.from_string('O+2H=H2O', self.species_dict),
            Reaction.from_string('O+H2=H2O', self.species_dict),
            Reaction.from_string('OH+H=H2O', self.species_dict),
            Reaction.from_string('OH+0.5H2=H2O', self.species_dict),
            Reaction.from_string('0.5O+2H=H2O', self.species_dict),
            Reaction.from_string('0.5O2+H2=H2O', self.species_dict)]
        )

        self.reactions_dict = {
            'class': "<class 'pMuTT.reaction.Reactions'>",
            'reactions': [{'bep': None,
                'class': "<class 'pMuTT.reaction.Reaction'>",
                'products': [{'T_high': 3500.0,
                              'T_low': 200.0,
                              'T_mid': 1000.0,
                              'a_high': [3.03399249,
                                         0.00217691804,
                                         -1.64072518e-07,
                                         -9.7041987e-11,
                                         1.68200992e-14,
                                         -30004.2971,
                                         4.9667701],
                              'a_low': [4.19864056,
                                        -0.0020364341,
                                        6.52040211e-06,
                                        -5.48797062e-09,
                                        1.77197817e-12,
                                        -30293.7267,
                                        -0.849032208],
                              'class': "<class 'pMuTT.empirical.nasa.Nasa'>",
                              'elements': {'H': 2, 'O': 1},
                              'name': 'H2O',
                              'notes': None,
                              'phase': None,
                              'references': None,
                              'statmech_model': None,
                              'mix_models': None}],
                'products_stoich': [1.0],
                'reactants': [{'T_high': 3500.0,
                               'T_low': 200.0,
                               'T_mid': 1000.0,
                               'a_high': [2.56942078,
                                          -8.59741137e-05,
                                          4.19484589e-08,
                                          -1.00177799e-11,
                                          1.22833691e-15,
                                          29217.5791,
                                          4.78433864],
                               'a_low': [3.1682671,
                                         -0.00327931884,
                                         6.64306396e-06,
                                         -6.12806624e-09,
                                         2.11265971e-12,
                                         29122.2592,
                                         2.05193346],
                               'class': "<class 'pMuTT.empirical.nasa.Nasa'>",
                               'elements': {'O': 1},
                               'name': 'O',
                               'notes': None,
                               'phase': None,
                               'references': None,
                               'statmech_model': None,
                               'mix_models': None},
                              {'T_high': 3500.0,
                               'T_low': 200.0,
                               'T_mid': 1000.0,
                               'a_high': [2.50000001,
                                          -2.30842973e-11,
                                          1.61561948e-14,
                                          -4.73515235e-18,
                                          4.98197357e-22,
                                          25473.6599,
                                          -0.446682914],
                               'a_low': [2.5,
                                         7.05332819e-13,
                                         -1.99591964e-15,
                                         2.30081632e-18,
                                         -9.27732332e-22,
                                         25473.6599,
                                         -0.446682853],
                               'class': "<class 'pMuTT.empirical.nasa.Nasa'>",
                               'elements': {'H': 1},
                               'name': 'H',
                               'notes': None,
                               'phase': None,
                               'references': None,
                               'statmech_model': None,
                               'mix_models': None}],
                'reactants_stoich': [1.0, 2.0],
                'transition_state': None,
                'transition_state_stoich': None},
               {'bep': None,
                'class': "<class 'pMuTT.reaction.Reaction'>",
                'products': [{'T_high': 3500.0,
                              'T_low': 200.0,
                              'T_mid': 1000.0,
                              'a_high': [3.03399249,
                                         0.00217691804,
                                         -1.64072518e-07,
                                         -9.7041987e-11,
                                         1.68200992e-14,
                                         -30004.2971,
                                         4.9667701],
                              'a_low': [4.19864056,
                                        -0.0020364341,
                                        6.52040211e-06,
                                        -5.48797062e-09,
                                        1.77197817e-12,
                                        -30293.7267,
                                        -0.849032208],
                              'class': "<class 'pMuTT.empirical.nasa.Nasa'>",
                              'elements': {'H': 2, 'O': 1},
                              'name': 'H2O',
                              'notes': None,
                              'phase': None,
                              'references': None,
                              'statmech_model': None,
                              'mix_models': None}],
                'products_stoich': [1.0],
                'reactants': [{'T_high': 3500.0,
                               'T_low': 200.0,
                               'T_mid': 1000.0,
                               'a_high': [2.56942078,
                                          -8.59741137e-05,
                                          4.19484589e-08,
                                          -1.00177799e-11,
                                          1.22833691e-15,
                                          29217.5791,
                                          4.78433864],
                               'a_low': [3.1682671,
                                         -0.00327931884,
                                         6.64306396e-06,
                                         -6.12806624e-09,
                                         2.11265971e-12,
                                         29122.2592,
                                         2.05193346],
                               'class': "<class 'pMuTT.empirical.nasa.Nasa'>",
                               'elements': {'O': 1},
                               'name': 'O',
                               'notes': None,
                               'phase': None,
                               'references': None,
                               'statmech_model': None,
                               'mix_models': None},
                              {'T_high': 3500.0,
                               'T_low': 200.0,
                               'T_mid': 1000.0,
                               'a_high': [3.3372792,
                                          -4.94024731e-05,
                                          4.99456778e-07,
                                          -1.79566394e-10,
                                          2.00255376e-14,
                                          -950.158922,
                                          -3.20502331],
                               'a_low': [2.34433112,
                                         0.00798052075,
                                         -1.9478151e-05,
                                         2.01572094e-08,
                                         -7.37611761e-12,
                                         -917.935173,
                                         0.683010238],
                               'class': "<class 'pMuTT.empirical.nasa.Nasa'>",
                               'elements': {'H': 2},
                               'name': 'H2',
                               'notes': None,
                               'phase': None,
                               'references': None,
                               'statmech_model': None,
                               'mix_models': None}],
                'reactants_stoich': [1.0, 1.0],
                'transition_state': None,
                'transition_state_stoich': None},
               {'bep': None,
                'class': "<class 'pMuTT.reaction.Reaction'>",
                'products': [{'T_high': 3500.0,
                              'T_low': 200.0,
                              'T_mid': 1000.0,
                              'a_high': [3.03399249,
                                         0.00217691804,
                                         -1.64072518e-07,
                                         -9.7041987e-11,
                                         1.68200992e-14,
                                         -30004.2971,
                                         4.9667701],
                              'a_low': [4.19864056,
                                        -0.0020364341,
                                        6.52040211e-06,
                                        -5.48797062e-09,
                                        1.77197817e-12,
                                        -30293.7267,
                                        -0.849032208],
                              'class': "<class 'pMuTT.empirical.nasa.Nasa'>",
                              'elements': {'H': 2, 'O': 1},
                              'name': 'H2O',
                              'notes': None,
                              'phase': None,
                              'references': None,
                              'statmech_model': None,
                              'mix_models': None}],
                'products_stoich': [1.0],
                'reactants': [{'T_high': 3500.0,
                               'T_low': 200.0,
                               'T_mid': 1000.0,
                               'a_high': [3.09288767,
                                          0.000548429716,
                                          1.26505228e-07,
                                          -8.79461556e-11,
                                          1.17412376e-14,
                                          3858.657,
                                          4.4766961],
                               'a_low': [3.99201543,
                                         -0.00240131752,
                                         4.61793841e-06,
                                         -3.88113333e-09,
                                         1.3641147e-12,
                                         3615.08056,
                                         -0.103925458],
                               'class': "<class 'pMuTT.empirical.nasa.Nasa'>",
                               'elements': {'H': 1, 'O': 1},
                               'name': 'OH',
                               'notes': None,
                               'phase': None,
                               'references': None,
                               'statmech_model': None,
                               'mix_models': None},
                              {'T_high': 3500.0,
                               'T_low': 200.0,
                               'T_mid': 1000.0,
                               'a_high': [2.50000001,
                                          -2.30842973e-11,
                                          1.61561948e-14,
                                          -4.73515235e-18,
                                          4.98197357e-22,
                                          25473.6599,
                                          -0.446682914],
                               'a_low': [2.5,
                                         7.05332819e-13,
                                         -1.99591964e-15,
                                         2.30081632e-18,
                                         -9.27732332e-22,
                                         25473.6599,
                                         -0.446682853],
                               'class': "<class 'pMuTT.empirical.nasa.Nasa'>",
                               'elements': {'H': 1},
                               'name': 'H',
                               'notes': None,
                               'phase': None,
                               'references': None,
                               'statmech_model': None,
                               'mix_models': None}],
                'reactants_stoich': [1.0, 1.0],
                'transition_state': None,
                'transition_state_stoich': None},
               {'bep': None,
                'class': "<class 'pMuTT.reaction.Reaction'>",
                'products': [{'T_high': 3500.0,
                              'T_low': 200.0,
                              'T_mid': 1000.0,
                              'a_high': [3.03399249,
                                         0.00217691804,
                                         -1.64072518e-07,
                                         -9.7041987e-11,
                                         1.68200992e-14,
                                         -30004.2971,
                                         4.9667701],
                              'a_low': [4.19864056,
                                        -0.0020364341,
                                        6.52040211e-06,
                                        -5.48797062e-09,
                                        1.77197817e-12,
                                        -30293.7267,
                                        -0.849032208],
                              'class': "<class 'pMuTT.empirical.nasa.Nasa'>",
                              'elements': {'H': 2, 'O': 1},
                              'name': 'H2O',
                              'notes': None,
                              'phase': None,
                              'references': None,
                              'statmech_model': None,
                              'mix_models': None}],
                'products_stoich': [1.0],
                'reactants': [{'T_high': 3500.0,
                               'T_low': 200.0,
                               'T_mid': 1000.0,
                               'a_high': [3.09288767,
                                          0.000548429716,
                                          1.26505228e-07,
                                          -8.79461556e-11,
                                          1.17412376e-14,
                                          3858.657,
                                          4.4766961],
                               'a_low': [3.99201543,
                                         -0.00240131752,
                                         4.61793841e-06,
                                         -3.88113333e-09,
                                         1.3641147e-12,
                                         3615.08056,
                                         -0.103925458],
                               'class': "<class 'pMuTT.empirical.nasa.Nasa'>",
                               'elements': {'H': 1, 'O': 1},
                               'name': 'OH',
                               'notes': None,
                               'phase': None,
                               'references': None,
                               'statmech_model': None,
                               'mix_models': None},
                              {'T_high': 3500.0,
                               'T_low': 200.0,
                               'T_mid': 1000.0,
                               'a_high': [3.3372792,
                                          -4.94024731e-05,
                                          4.99456778e-07,
                                          -1.79566394e-10,
                                          2.00255376e-14,
                                          -950.158922,
                                          -3.20502331],
                               'a_low': [2.34433112,
                                         0.00798052075,
                                         -1.9478151e-05,
                                         2.01572094e-08,
                                         -7.37611761e-12,
                                         -917.935173,
                                         0.683010238],
                               'class': "<class 'pMuTT.empirical.nasa.Nasa'>",
                               'elements': {'H': 2},
                               'name': 'H2',
                               'notes': None,
                               'phase': None,
                               'references': None,
                               'statmech_model': None,
                               'mix_models': None}],
                'reactants_stoich': [1.0, 0.5],
                'transition_state': None,
                'transition_state_stoich': None},
               {'bep': None,
                'class': "<class 'pMuTT.reaction.Reaction'>",
                'products': [{'T_high': 3500.0,
                              'T_low': 200.0,
                              'T_mid': 1000.0,
                              'a_high': [3.03399249,
                                         0.00217691804,
                                         -1.64072518e-07,
                                         -9.7041987e-11,
                                         1.68200992e-14,
                                         -30004.2971,
                                         4.9667701],
                              'a_low': [4.19864056,
                                        -0.0020364341,
                                        6.52040211e-06,
                                        -5.48797062e-09,
                                        1.77197817e-12,
                                        -30293.7267,
                                        -0.849032208],
                              'class': "<class 'pMuTT.empirical.nasa.Nasa'>",
                              'elements': {'H': 2, 'O': 1},
                              'name': 'H2O',
                              'notes': None,
                              'phase': None,
                              'references': None,
                              'statmech_model': None,
                              'mix_models': None}],
                'products_stoich': [1.0],
                'reactants': [{'T_high': 3500.0,
                               'T_low': 200.0,
                               'T_mid': 1000.0,
                               'a_high': [2.56942078,
                                          -8.59741137e-05,
                                          4.19484589e-08,
                                          -1.00177799e-11,
                                          1.22833691e-15,
                                          29217.5791,
                                          4.78433864],
                               'a_low': [3.1682671,
                                         -0.00327931884,
                                         6.64306396e-06,
                                         -6.12806624e-09,
                                         2.11265971e-12,
                                         29122.2592,
                                         2.05193346],
                               'class': "<class 'pMuTT.empirical.nasa.Nasa'>",
                               'elements': {'O': 1},
                               'name': 'O',
                               'notes': None,
                               'phase': None,
                               'references': None,
                               'statmech_model': None,
                               'mix_models': None},
                              {'T_high': 3500.0,
                               'T_low': 200.0,
                               'T_mid': 1000.0,
                               'a_high': [2.50000001,
                                          -2.30842973e-11,
                                          1.61561948e-14,
                                          -4.73515235e-18,
                                          4.98197357e-22,
                                          25473.6599,
                                          -0.446682914],
                               'a_low': [2.5,
                                         7.05332819e-13,
                                         -1.99591964e-15,
                                         2.30081632e-18,
                                         -9.27732332e-22,
                                         25473.6599,
                                         -0.446682853],
                               'class': "<class 'pMuTT.empirical.nasa.Nasa'>",
                               'elements': {'H': 1},
                               'name': 'H',
                               'notes': None,
                               'phase': None,
                               'references': None,
                               'statmech_model': None,
                               'mix_models': None}],
                'reactants_stoich': [0.5, 2.0],
                'transition_state': None,
                'transition_state_stoich': None},
               {'bep': None,
                'class': "<class 'pMuTT.reaction.Reaction'>",
                'products': [{'T_high': 3500.0,
                              'T_low': 200.0,
                              'T_mid': 1000.0,
                              'a_high': [3.03399249,
                                         0.00217691804,
                                         -1.64072518e-07,
                                         -9.7041987e-11,
                                         1.68200992e-14,
                                         -30004.2971,
                                         4.9667701],
                              'a_low': [4.19864056,
                                        -0.0020364341,
                                        6.52040211e-06,
                                        -5.48797062e-09,
                                        1.77197817e-12,
                                        -30293.7267,
                                        -0.849032208],
                              'class': "<class 'pMuTT.empirical.nasa.Nasa'>",
                              'elements': {'H': 2, 'O': 1},
                              'name': 'H2O',
                              'notes': None,
                              'phase': None,
                              'references': None,
                              'statmech_model': None,
                              'mix_models': None}],
                'products_stoich': [1.0],
                'reactants': [{'T_high': 3500.0,
                               'T_low': 200.0,
                               'T_mid': 1000.0,
                               'a_high': [3.28253784,
                                          0.00148308754,
                                          -7.57966669e-07,
                                          2.09470555e-10,
                                          -2.16717794e-14,
                                          -1088.45772,
                                          5.45323129],
                               'a_low': [3.78245636,
                                         -0.00299673416,
                                         9.84730201e-06,
                                         -9.68129509e-09,
                                         3.24372837e-12,
                                         -1063.94356,
                                         3.65767573],
                               'class': "<class 'pMuTT.empirical.nasa.Nasa'>",
                               'elements': {'O': 2},
                               'name': 'O2',
                               'notes': None,
                               'phase': None,
                               'references': None,
                               'statmech_model': None,
                               'mix_models': None},
                              {'T_high': 3500.0,
                               'T_low': 200.0,
                               'T_mid': 1000.0,
                               'a_high': [3.3372792,
                                          -4.94024731e-05,
                                          4.99456778e-07,
                                          -1.79566394e-10,
                                          2.00255376e-14,
                                          -950.158922,
                                          -3.20502331],
                               'a_low': [2.34433112,
                                         0.00798052075,
                                         -1.9478151e-05,
                                         2.01572094e-08,
                                         -7.37611761e-12,
                                         -917.935173,
                                         0.683010238],
                               'class': "<class 'pMuTT.empirical.nasa.Nasa'>",
                               'elements': {'H': 2},
                               'name': 'H2',
                               'notes': None,
                               'phase': None,
                               'references': None,
                               'statmech_model': None,
                               'mix_models': None}],
                'reactants_stoich': [0.5, 1.0],
                'transition_state': None,
                'transition_state_stoich': None}]}

    def test_get_species(self):
        self.assertDictEqual(self.reactions.get_species(key='name'), 
                             self.species_dict)

    def test_to_dict(self):
        self.assertEqual(self.reactions.to_dict(), self.reactions_dict)

    def test_from_dict(self):
        self.assertEqual(Reactions.from_dict(self.reactions_dict),
                         self.reactions)

if __name__ == '__main__':
    unittest.main()
