import great_expectations as gx
import pandas as pd
import os


def validate_file(path_file):

    # Leer el archivo CSV
    df = pd.read_csv(path_file)
    context = gx.get_context()

    if "pandas" in context.data_sources:
        data_source = context.data_sources["pandas"]
    else:
        data_source = context.data_sources.add_pandas("pandas")

    data_asset = data_source.add_dataframe_asset(name="pd dataframe asset")

    batch_definition = data_asset.add_batch_definition_whole_dataframe("batch definition")
    batch = batch_definition.get_batch(batch_parameters={"dataframe": df})
    expectation = gx.expectations.ExpectColumnValuesToBeBetween(
        column="passenger_count", min_value=1, max_value=6
    )
    validation_result = batch.validate(expectation)
    print(validation_result)


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.realpath(__file__))

    csv_file_path = os.path.join(script_dir, '../data/raw/data_to_validate.csv')
    validate_file(csv_file_path)
