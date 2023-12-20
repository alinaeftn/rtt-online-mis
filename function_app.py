import azure.functions as func
import logging
from frictionless import Resource, transform, steps


def transform_resource(resource: Resource) -> Resource:
    return transform(resource, steps=[steps.row_filter(formula="c1_g > 0")])

def process_raw_excel(raw_data: bytes) -> bytes:
    # init resource
    resource = Resource(raw_data, format="xlsx")

    # apply transformation
    transformed_resource = transform_resource(resource)

    # retrieve transformed binary data
    output = transformed_resource.write(format="xlsx", scheme="buffer")
    return output.data


app = func.FunctionApp()

@app.blob_trigger(arg_name="blob", path="inputcontainer/{name}",
                               connection="BlobStorageConnectionString")
@app.blob_input(arg_name="inputblob", path="inputcontainer/{name}",
                            connection="BlobStorageConnectionString", data_type=func.DataType.BINARY)
@app.blob_output(arg_name="outputblob", path="outputcontainer/{name}",
                             connection="BlobStorageConnectionString", data_type=func.DataType.BINARY)
def blob_trigger(blob: func.InputStream, inputblob: bytes, outputblob: func.Out[bytes]):
    logging.info(f"Python blob trigger function starting for blob: "
                f"Name: {blob.name}")
    logging.info(f"Contents: {inputblob}")
    outputblob.set(process_raw_excel(inputblob))

