import os
import sys




class copy_and_convert_temps(object):


  def run_it(self):
    copy_and_convert_temps().do_them_together()


  def do_them_together(self):
    with open("first.txt", "r") as f1:
      with open("second.txt", "w") as f2: 
        f2.writelines(copy_and_convert_temps().convert_temps(f1))   
   

  def convert_temps(self, temp):
    for xi in temp:
      f_to_c = 9.0/5.0 * int(xi) + 32
      
      yield (str(f_to_c) + "\n")
        

copy_and_convert_temps().run_it()
