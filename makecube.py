
import astropy.io.fits as fits
specids = ["047", "051", "055", "060", "064", "068", "072", "076", "080", "084", "136", "088", "092", "121", "125", "130", "140", "144"]
for specid in specids:
    hdu, = fits.open("spec{}-oiii.fits".format(specid))
    print [hdu.header["NAXIS"+s] for s in "12"]
