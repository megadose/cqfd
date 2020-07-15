import argparse,csv
from cqfd import *
parser = argparse.ArgumentParser()
required = parser.add_argument_group('required arguments')
parser.add_argument('-n','--name',help="Target Name",required=True)
parser.add_argument('-o','--output',help="Name of the csv output file",required=True)

args = parser.parse_args()
result = cqfd(args.name)
if len(result)!=0:
    keys = result[0].keys()
    with open(str(args.output), 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        for data in result:
            writer.writerow(data)
    print("You can see the output in "+str(args.output))
else:
    print("Sorry, but no skype account was found with that name.")
    exit()
