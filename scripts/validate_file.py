import great_expectations as gx
import pandas as pd
import datetime
import os


def validate_file(path_file):

    # Leer el archivo CSV
    df = pd.read_csv(path_file)
    context = gx.get_context()

    # Generar un nombre único basado en la fecha y hora actual
    current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    data_source_name = f"pandas_{current_time}"

    data_source = context.data_sources.add_pandas(data_source_name)

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
