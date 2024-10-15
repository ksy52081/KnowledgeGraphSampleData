from common.util import parse_main_args
from generator.convergence_data_generator import ConvergenceDataGenerator
from runner.collaborative_filtering_association_analysis_runner import AssociationRuleCFRunner

if __name__ == "__main__":
  args = parse_main_args()
  mode = args["mode"]
  algorithm = args["algorithm"]

  if mode == "mock":
    mock_input_file_path = '/mnt/data/mock_shopping_cart.csv'
    temp_output_file_path = '/mnt/data/association_rules.csv'

    generator = ConvergenceDataGenerator()
    generator.generateDataFrameWithFilePath(mock_input_file_path)
    args["input_data_path"] = mock_input_file_path

    if args["output_data_path"] is None:
      args["output_data_path"] = temp_output_file_path

  if algorithm == "association-analysis":
    runner = AssociationRuleCFRunner(args)
    runner.run()