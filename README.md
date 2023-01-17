-------------------------
Readme file for DiSCUS
Angel Goni-Moreno
-------------------------

ABOUT
	DiSCUS is a simulator for bacterial populations in discrete space/time
	focused on the study of Horizontal Gene Transfer.
	anandgel@gmail.com, MIT License

	This release is the first developers' version of the code (2012) with an
	update (2023) to match pymunk 4 requirements. 

	Email: anandgel@gmail.com

	Tested under Linux, Windows and MacOS

REQUIREMENTS

	* Python (www.python.org. The code has been developed in version 2.7)
	* Pygame (www.pygame.org - Python library)
	* Scipy (www.scipy.org - Python library)
	* NumPy (www.scipy.org - Python library)
	* Pymunk (www.pymunk.org - Physics engine. The code has been tested for
	  versions 2.0 and 4.0 so we recommend to install those ones. In the
	  pymunk site there is an installation guide)


HOW TO USE

	The example files (cross.py, pipe.py and plain.py) make use of the main
	program (discus.py) in order to run the simulation. The parameters and
	definitions are in files included in the Imports folder

	After installing all required tools, type the next line to run example
	"cross":

		> python cross.py

	Without modification, the simulation will show growing cells in a cross-shaped
	channel. The donors (left) have an oscillator inside which will be transferred
	to recipients (right at the beginning)

	Type the next line to run the "pipe" example:
		
		> python pipe.py

	Without modification, the simulation will show growing cells in a
	longitudinal channel. One strain (recipient strain from cross.py) is simulated

	Type the next line to run the "plain" example:

		> python plain.py

	Without modification, the "plain" example will display an empty space
	(no walls) where empy cells (genetic circuit set to NONE) grow.
