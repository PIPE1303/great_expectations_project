# from great_expectations.data_context import DataContext
import great_expectations as gx
import pandas as pd


def validate_file(file_path):
    df = pd.read_csv(
        f"{file_path}"
    )
    context = gx.get_context()
    data_source = context.data_sources.add_pandas("pandas")
    data_asset = data_source.add_dataframe_asset(name="pd dataframe asset")

    batch_definition = data_asset.add_batch_definition_whole_dataframe("batch def")
    batch = batch_definition.get_batch(batch_parameters={"dataframe": df})
    expectation = gx.expectations.ExpectColumnValuesToBeBetween(
        column="passenger_count", min_value=1, max_value=6
    )
    validation_result = batch.validate(expectation)
    print(validation_result)

    # context = DataContext("great_expectations/")
    # checkpoint_name = "file_validation_checkpoint"

    # # Configurar un punto de validación
    # checkpoint = context.test_yaml_config(
    #     f"""
    #     name: {checkpoint_name}
    #     config_version: 1.0
    #     validations:
    #       - batch_request:
    #           datasource_name: data_dir
    #           data_connector_name: default_inferred_data_connector_name
    #           data_asset_name: {file_path}
    #         expectation_suite_name: file_suite
    #     """
    # )

    # results = checkpoint.run()

    # if results["success"]:
    #     print(f"Validation succeeded for {file_path}")
    # else:
    #     print(f"Validation failed for {file_path}")
    #     raise ValueError("Validation failed!")


if __name__ == "__main__":
    validate_file("data/raw/data_to_validate.csv")
