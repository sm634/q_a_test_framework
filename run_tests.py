from tests.test_discovery_connector import test_discovery_connection
# from tests.test_ir_metrics import test_ir_metrics
import argparse


# Create an ArgumentParser object
parser = argparse.ArgumentParser(description="choose the test you want to run")
parser.add_argument('--test_function',
                    type=str,
                    choices=['test_discovery_connection', 'test_ir_metrics'],
                    default='test_discovery_connection')

# parse arguments
args = parser.parse_args()

# function to test
test_function = args.test_function

def run_test():
    if test_function == 'test_discovery_connection':
        response = test_discovery_connection()
        

run_test()
