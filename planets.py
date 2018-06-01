#!/usr/bin/python3


# Global constants
GRAVITAIONAL_CONSTANT = 6.67E-11
MASS_OF_SUN = 1.989E30
MASS_OF_EARTH = 5.972E24
DISTANCE_OF_EARTH_FROM_SUN = 1.496E11


class Universe(object):
	pass


class Galaxy(Universe):
	def __init__(self, name):
		self.name = name


class Star(object):
	def __init__(self, name, galaxy, mass=0):
		self.name = name
		self.galaxy = galaxy
		self.mass = mass

	def __str__(self):
		return "{} belongs to {}".format(self.name, self.galaxy)


class Planet(object):
	def __init__(self, name, star, mass=0, distance_from_star=0):
		self.name = name
		self.star = star
		self.mass = mass
		self.distance_from_star = distance_from_star

	def gravitation_force(self):
		return GRAVITAIONAL_CONSTANT*((self.mass*self.star.mass)/self.distance_from_star**2)

	def __str__(self):
		return "{} belongs to {}".format(self.name, self.star)


if __name__ == '__main__':
	# create a galaxy 'Milky Way'
	milkyWay = Galaxy('Milky Way') 
	# Create a star in galaxy 'Sun' in 'Milky Way'
	sun = Star('Sun', milkyWay, mass=MASS_OF_SUN)
	# creae a planet 'Earth' in 'Milky Way' which belongs to star 'Sun'
	earth = Planet('Earth', sun, mass=MASS_OF_EARTH, distance_from_star=DISTANCE_OF_EARTH_FROM_SUN)	
	print(earth.gravitation_force())

	# From Mercury

	# To Pluto (Planet???)