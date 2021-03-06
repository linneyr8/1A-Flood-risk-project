"""Contains function for the polynomial fitting on data"""
import numpy as np
from matplotlib.dates import date2num 

def polyfit(dates, levels, p):
  """Function that finds the least-square fit polynomial from 
  
  Args:
     dates (list): The list of dates for the x-axis
     level (list): The corresponding water levels for each date for the y-axis
     p (integer): degree of the polynomial that is desired
   
   Returns:
      numpy poly1d object: Contains the coefficients of the resulting polynomial 
      float: The number of days since the origin of the Gregporain Calendar that was shifted to find the polynomial."""
  dates_num = date2num(dates)
  x = [date - dates_num[-1] for date in dates_num]
  y = levels
  p_coeff = np.polyfit(x, y, p)
  poly = np.poly1d(p_coeff)
  return poly, dates_num[-1]
