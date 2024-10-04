import argparse

def parse_main_args():
  parser = argparse.ArgumentParser()

  parser.add_argument("--testargs", type=str, help="str")

  args = parser.parse_known_args()[0]

  return vars(args)