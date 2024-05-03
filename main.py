from scripts.run_vodafone_discovery_test import run_vodafone_test, custom_preprocess
# from tests.test_ir_metrics import test_ir_metrics
import argparse


# Create an ArgumentParser object
parser = argparse.ArgumentParser(description="choose the test you want to run")
parser.add_argument('--test_script',
                    type=str,
                    choices=['run_discovery_test'],
                    default='run_discovery_test')

# parse arguments
args = parser.parse_args()

# script to run
test_script = args.test_script

def main():
    if test_script == 'run_discovery_test':
        run_vodafone_test()
        

if __name__ == '__main__':
    main()
