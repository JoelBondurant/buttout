#!/usr/bin/env python3
import argparse
import subprocess as sp


def buttin():
	sp.call(['sudo','cp','/etc/hosts.mine','/etc/hosts'])

def buttout():
	sp.call('sudo su -c "cat hosts.snoops >> /etc/hosts"', shell = True)

def main():
	desc = """Buttout, a utility to control prolific invasive webscale
		snooping / aka online advertising."""
	argparser = argparse.ArgumentParser(add_help = True, description = desc)
	argparser.add_argument('-o', '--buttout', action = 'store_true', default = True, help = 'Buttout peeping toms.')
	argparser.add_argument('-i', '--buttin', action = 'store_true', default = False, help = 'No internet filtering.')
	args = argparser.parse_args()
	if args.buttin:
		buttin()
	elif args.buttout:
		buttout()

if __name__ == '__main__':
	main()
