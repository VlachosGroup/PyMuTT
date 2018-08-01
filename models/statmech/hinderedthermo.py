# -*- coding: utf-8 -*-

import numpy as np
from ase import thermochemistry
from Thermochemistry import constants as c
from Thermochemistry.models.statmech.heat_capacity import get_CvoR_trans, get_CvoR_vib, get_CvoR_rot

class HinderedThermo:
	"""
	Hindered translator/hindered rotor model. 
	Used for surface species where there are 2 translational modes,
	1 rotational mode perpendicular to the surface, and 3N-3 vibrational modes.

	See further documentation from the ASE implementation. 
	https://wiki.fysik.dtu.dk/ase/ase/thermochemistry/thermochemistry.html#hindered-translator-hindered-rotor-model

	Attributes
		model - ase.Thermochemistry.HinderedThermo object
			The Hindered Thermo object has the following attributes.
				vib_energies - (3N,) ndarray where N is number of atoms
					Vibrational energies in eV.
				trans_barrier_energy - float
					Translational energy barrier in eV.
				rot_barrier_energy - float
					Rotational energy barrier in eV
				sitedensity - float
					Site density in cm^-2
				rotationalminima - int
					Number of equivalent minima for an adsorbate full rotation
					e.g. 6 for an adsorbate on an fcc(111) top site
				potentialenergy - float
					Potential energy in eV
				atoms - ase.Atoms object
					Used to calculate mass and inertia
				symmetrynumber - int
					Symmetry number of adsorbate. 
		            Reference point group/symmetry number table:
		            Point group    symmetry number
		            C1             1
		            Cs             1
		            C2             2
		            C2v            2
		            C3v            3
		            Cinfv          1
		            D2h            4
		            D3h            6
		            D5h            10
		            Dinfh          2
		            D3d            6
		            Td             12
		            Oh             24
		            See DOI for more details: 10.1007/s00214-007-0328-0
				mass - float
					Mass of adsorbate in amu. If unspecified, uses the atoms object
				inertia - float
					Reduced moment of inertia in amu*A^-2. If unspecified, uses atoms object
	"""
	def __init__(self, vib_energies, trans_barrier_energy, rot_barrier_energy, sitedensity, rotationalminima, potentialenergy=0.0, mass=None, inertia=None, atoms=None, symmetrynumber=1):
		self.model = thermochemistry.HinderedThermo(
			vib_energies=vib_energies,
			trans_barrier_energy=trans_barrier_energy,
			rot_barrier_energy=rot_barrier_energy,
			sitedensity=sitedensity,
			rotationalminima=rotationalminima,
			potentialenergy=potentialenergy,
			mass=mass,
			inertia=inertia,
			atoms=atoms,
			symmetrynumber=symmetrynumber)

	def get_CpoR(self, Ts):
		"""
		Calculates the dimensionless heat capacity (Cp/R) at a given temperature.
		If you would like to use different behavior from the default, the
		thermo_model used must have the function 'get_CpoR'.

		Parameters
			Ts - array-like or scalar
				Temperature(s) in K
		Returns
			float or (N,) ndarray
				Dimensionless heat capacity (Cp/R)
		"""
		raise NotImplementedError

	def get_HoRT(self, Ts, verbose=False):
		"""
		Returns the dimensionless enthalpy at a given temperature

		Parameters
			Ts - float or (N,) ndarray
				Temperature(s) in K
			verbose - bool
				Whether a table breaking down each contribution should be printed
		Returns
			float or (N,) ndarray
				Dimensionless heat capacity (H/RT) at the specified temperature
		"""
		try:
			iter(Ts)
		except TypeError:
			HoRT = self.model.get_internal_energy(temperature=Ts, verbose=verbose)/(c.kb('eV/K') * Ts)
		else:
			HoRT = np.zeros_like(Ts)
			for i, T in enumerate(Ts):
				HoRT[i] = self.model.get_internal_energy(temperature=T, verbose=verbose)/(c.kb('eV/K') * T)
		return HoRT


	def get_SoR(self, Ts, P=1., verbose=False):
		"""
		Returns the dimensionless entropy at a given temperature and pressure

		Parameters
			Ts - float or (N,) ndarray
				Temperature(s) in K
			P - float
				Pressure in atm
			verbose - bool
				Whether a table breaking down each contribution should be printed
		Returns
			float or (N,) ndarray
				Dimensionless entropy (S/R) at the specified temperature and pressure
		"""
		try:
			iter(Ts)
		except TypeError:
			SoR = self.model.get_entropy(temperature=Ts, verbose=verbose)/c.R('eV/K')
		else:
			SoR = np.zeros_like(Ts)
			for i, T in enumerate(Ts):
				SoR[i] = self.model.get_entropy(temperature=T, verbose=verbose)/c.R('eV/K')
		return SoR

	def get_GoRT(self, Ts, P=1., verbose=False):
		"""
		Returns the dimensionless Gibbs energy at a given temperature

		Parameters
			Ts - float or (N,) ndarray
				Temperature(s) in K
			P - float
				Pressure in bar
			verbose - bool
				Whether a table breaking down each contribution should be printed
		Returns
			float or (N,) ndarray
				Dimensionless heat capacity (G/RT) at the specified temperature
		"""
		try:
			iter(Ts)
		except TypeError:
			GoRT = self.model.get_helmholtz_energy(temperature=Ts, pressure=P*c.convert_unit(from_='bar', to='Pa'), verbose=verbose)/(c.kb('eV/K') * Ts)
		else:
			GoRT = np.zeros_like(Ts)
			for i, T in enumerate(Ts):
				GoRT[i] = self.model.get_helmholtz_energy(temperature=T, pressure=P*c.convert_unit(from_='bar', to='Pa'), verbose=verbose)/(c.kb('eV/K') * T)
		return GoRT