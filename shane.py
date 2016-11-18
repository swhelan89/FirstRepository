import os
import re
import sys
import types
import copy_reg
import multiprocessing



class copy_and_convert_temps(object):

  def ct_worker(self, temp):
    return temp 
  
  def ct_handler(self):
    cpus = multiprocessing.cpu_count()
    p = multiprocessing.Pool(cpus)
    c_t = []

    with open("first.txt", "r") as f1:
      temp = [x1 for x1 in (y1 for y1 in f1) if x1]
      for x2 in temp:
        c_t.append(self.convert_temps(x2))
      with open("second.txt", "w") as f2: 
        for r in p.imap(self.ct_worker, c_t):   
          f2.write(r)

  def convert_temps(self, temp):
    for xi in temp:
      f_to_c = 9.0/5.0 * int(xi) + 32
      
      return (str(f_to_c) + "\n")



def _p_method(m):
    if m.im_self is None:
        return getattr, (m.im_class, m.im_func.func_name)
    else:
        return getattr, (m.im_self, m.im_func.func_name)

copy_reg.pickle(types.MethodType, _p_method)

        

copy_and_convert_temps().ct_handler()
