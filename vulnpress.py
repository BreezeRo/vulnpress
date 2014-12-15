import argparse
from exploits.exploitsql import ExploitSql
from exploits.exploitshell import ExploitShell

parser = argparse.ArgumentParser()
parser.add_argument('hostname', help='URL')
parser.add_argument('category', help='sql, shell')
args = parser.parse_args()

if args.hostname and args.category:
	hostname = args.hostname
	category = args.category
	if category == 'sql':
		[cls.exploit(cls, hostname) for cls in vars()['ExploitSql'].__subclasses__()]
	if category == 'shell':
		[cls.exploit(cls, hostname) for cls in vars()['ExploitShell'].__subclasses__()]